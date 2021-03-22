#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <pulse/simple.h>
#include <pulse/error.h>
#include <pulse/pulseaudio.h>
#include <pthread.h>

struct audio_data {
    int FFTbufferSize;
    __int16_t audio_out_r[65536];
    __int16_t audio_out_l[65536];
    int format;
    unsigned int rate;
    char *source; //alsa device, fifo path or pulse source
    int im; //input mode alsa, fifo or pulse
    int channels;
    int terminate; // shared variable used to terminate audio thread
    int resp_size;
    char error_message[1024];
};



pa_mainloop *m_pulseaudio_mainloop;


void cb(__attribute__((unused)) pa_context *pulseaudio_context, const pa_server_info *i, void *userdata) {

    //getting default sink name
    struct audio_data *audio = (struct audio_data *) userdata;
    audio->source = (char *) malloc(sizeof(char) * 1024);

    strcpy(audio->source, i->default_sink_name);

    //appending .monitor suufix
    audio->source = strcat(audio->source, ".monitor");

    //quiting mainloop
    pa_context_disconnect(pulseaudio_context);
    pa_context_unref(pulseaudio_context);
    pa_mainloop_quit(m_pulseaudio_mainloop, 0);
    pa_mainloop_free(m_pulseaudio_mainloop);
}

void pulseaudio_context_state_callback(pa_context *pulseaudio_context, void *userdata) {

    //make sure loop is ready
    switch (pa_context_get_state(pulseaudio_context)) {
        case PA_CONTEXT_UNCONNECTED:
            //printf("UNCONNECTED\n");
            break;
        case PA_CONTEXT_CONNECTING:
            //printf("CONNECTING\n");
            break;
        case PA_CONTEXT_AUTHORIZING:
            //printf("AUTHORIZING\n");
            break;
        case PA_CONTEXT_SETTING_NAME:
            //printf("SETTING_NAME\n");
            break;
        case PA_CONTEXT_READY://extract default sink name
            //printf("READY\n");
            pa_operation_unref(pa_context_get_server_info(pulseaudio_context, cb, userdata));
            break;
        case PA_CONTEXT_FAILED:
            printf("failed to connect to pulseaudio server\n");
            exit(EXIT_FAILURE);
            break;
        case PA_CONTEXT_TERMINATED:
//            printf("TERMINATED\n");
            pa_mainloop_quit(m_pulseaudio_mainloop, 0);
            break;
    }
}

void getPulseDefaultSink(void *data) {

    struct audio_data *audio = (struct audio_data *) data;
    pa_mainloop_api *mainloop_api;
    pa_context *pulseaudio_context;
    int ret;

    // Create a mainloop API and connection to the default server
    m_pulseaudio_mainloop = pa_mainloop_new();

    mainloop_api = pa_mainloop_get_api(m_pulseaudio_mainloop);
    pulseaudio_context = pa_context_new(mainloop_api, "q device list");


    // This function connects to the pulse server
    pa_context_connect(pulseaudio_context, NULL, PA_CONTEXT_NOFLAGS, NULL);


//        printf("connecting to server\n");

    //This function defines a callback so the server will tell us its state.
    pa_context_set_state_callback(pulseaudio_context, pulseaudio_context_state_callback, (void *) audio);



    //starting a mainloop to get default sink

    //starting with one nonblokng iteration in case pulseaudio is not able to run
    if (!(ret = pa_mainloop_iterate(m_pulseaudio_mainloop, 0, &ret))) {
        printf("Could not open pulseaudio mainloop to "
               "find default device name: %d\n"
               "check if pulseaudio is running\n",
               ret);

        exit(EXIT_FAILURE);
    }

    pa_mainloop_run(m_pulseaudio_mainloop, &ret);


}



pa_simple *open_input_stream(void *data, int *resp) {

    struct audio_data *audio = (struct audio_data *) data;

    int buffer_size = audio->FFTbufferSize;





    /* The sample type to use */
    pa_sample_spec ss = {
            .format = PA_SAMPLE_S16LE,
            .rate =  44100,
            .channels = (uint8_t) 2
    };
    pa_buffer_attr pb = {
            .maxlength = (uint32_t) buffer_size * 2, //BUFSIZE * 2,
            .fragsize = (uint32_t) buffer_size
    };

    pa_simple *s = NULL;
    int error;

    if (!(s = pa_simple_new(NULL, "q", PA_STREAM_RECORD, audio->source, "audio for qsoundbars", &ss, NULL, &pb, &error))) {
        sprintf(audio->error_message,
                __FILE__": Could not open pulseaudio source: %s, %s. \
		To find a list of your pulseaudio sources run 'pacmd list-sources'\n",
                audio->source, pa_strerror(error));

        audio->terminate = 1;
//        fclose(fp);
        pthread_exit(NULL);
    }


    return s;

}

void read_input_stream(pa_simple *s, void *data, int *resp) {
    struct audio_data *audio = (struct audio_data *) data;
    int buffer_size = audio->FFTbufferSize;


    int16_t buffer[buffer_size /2 ];

    int n = 0, i, error;


    if (pa_simple_read(s, buffer, sizeof(buffer), &error) < 0) {
        sprintf(audio->error_message, __FILE__": pa_simple_read() failed: %s\n", pa_strerror(error));
        audio->terminate = 1;
        pthread_exit(NULL);
    }

    for (i = 0; i < audio->resp_size; i++) resp[i] = 0;

    for (int i = 0; i < buffer_size/2 ; i += 2) {
//        audio->audio_out_l[n] = buffer[i];
//        audio->audio_out_r[n] = buffer[i + 1];

        if (audio->channels == 1) {
            resp[n] = buffer[i];
        } else{
            resp[n] = (buffer[i] + buffer[i + 1]) / 2;
        }


        n++;
        if (n == audio->resp_size) n = 0;

    }


//    for (int c = 0; c < buffer_size/2; c++) {
//        if (audio->channels == 1) {
//            resp[c] = (audio->audio_out_l[c]);
//        } else {
//            resp[c] = (audio->audio_out_l[c] + audio->audio_out_r[c]) / 2;
//        }
//    }


}

void close_input_stream(pa_simple *s) {
    pa_simple_free(s);
}
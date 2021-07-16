#include <stdio.h>
#include "pulse.c"


struct audio_data audio;

pa_simple *conn = NULL;
int *resp;

int _is_open = 0;


int is_open() {
    return _is_open;
}

int open_stream(int buffer_size, int channels) {
    if (conn == NULL){
        audio.FFTbufferSize = (buffer_size *2);
        audio.resp_size = (buffer_size);
        audio.channels = channels;
        resp = (int *) malloc(sizeof(int) * (buffer_size) );

        getPulseDefaultSink(&audio);
        conn = open_input_stream(&audio, resp);
    }

    if (conn != NULL) {
        _is_open = 1;
    }

    return _is_open;
}

int *read_stream() {
    if (conn != NULL) {
        read_input_stream(conn, &audio, resp);
    }
    return resp;
}

void close_stream() {
    if (conn != NULL) {
        close_input_stream(conn);
        free(resp);
    }
    _is_open = 0;
    conn = NULL;
}

int *get_resp() {
    audio.terminate = 1;

    getPulseDefaultSink(&audio);

//    printf("Name: %s\n", audio.source);

//    input_pulse2(&audio, resp, 0);

    return resp;
}

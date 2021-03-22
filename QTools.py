def qprint(*args, color="info", bold=False, blink=False):
    colors = {
        'reset': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'blink': '\033[5m',

        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
    }
    colors['info'] = colors['cyan'] + " - "

    
    if color in colors.keys(): print(colors[color], end='')
    if blink: print(colors['blink'], end='')
    if bold: print(colors['bold'], end='')

    print(*args, sep=' ', end= colors['reset'] + '\n', flush=True)


class Easing(object):
    from math import sqrt, pow, sin, cos
    from math import pi as M_PI
    M_PI_2 = M_PI * 2

    '''
    original c code:
    https://raw.githubusercontent.com/warrenm/AHEasing/master/AHEasing/easing.c
    Copyright (c) 2011, Auerhaus Development, LLC
    http://sam.zoy.org/wtfpl/COPYING for more details.
    '''

    #  Modeled after the line y = x
    def LinearInterpolation(p):
        return p

    # Modeled after the parabola y = x^2
    def QuadraticEaseIn(p):
        return p * p

    # Modeled after the parabola y = -x^2 + 2x
    def QuadraticEaseOut(p):
        return -(p * (p - 2))

    # Modeled after the piecewise quadratic
    # y = (1/2)((2x)^2)             ; [0, 0.5)
    # y = -(1/2)((2x-1)*(2x-3) - 1) ; [0.5, 1]
    def QuadraticEaseInOut(p):
        if (p < 0.5):
            return 2 * p * p
        return (-2 * p * p) + (4 * p) - 1

    # Modeled after the cubic y = x^3
    def CubicEaseIn(p):
        return p * p * p

    # Modeled after the cubic y = (x - 1)^3 + 1
    def CubicEaseOut(p):
        f = (p - 1)
        return f * f * f + 1

    # Modeled after the piecewise cubic
    # y = (1/2)((2x)^3)       ; [0, 0.5)
    # y = (1/2)((2x-2)^3 + 2) ; [0.5, 1]
    def CubicEaseInOut(p):
        if (p < 0.5):
            return 4 * p * p * p
        else:
            f = ((2 * p) - 2)
            return 0.5 * f * f * f + 1

    # Modeled after the quartic x^4
    def QuarticEaseIn(p):
        return p * p * p * p

    # Modeled after the quartic y = 1 - (x - 1)^4
    def QuarticEaseOut(p):
        f = (p - 1)
        return f * f * f * (1 - p) + 1

    # Modeled after the piecewise quartic
    # y = (1/2)((2x)^4)        ; [0, 0.5)
    # y = -(1/2)((2x-2)^4 - 2) ; [0.5, 1]
    def QuarticEaseInOut(p) :
        if (p < 0.5):
            return 8 * p * p * p * p
        else:
            f = (p - 1)
            return -8 * f * f * f * f + 1
        


    # Modeled after the quintic y = x^5
    def QuinticEaseIn(p):
        return p * p * p * p * p

    # Modeled after the quintic y = (x - 1)^5 + 1
    def QuinticEaseOut(p):
        f = (p - 1)
        return f * f * f * f * f + 1


    # Modeled after the piecewise quintic
    # y = (1/2)((2x)^5)       ; [0, 0.5)
    # y = (1/2)((2x-2)^5 + 2) ; [0.5, 1]
    def QuinticEaseInOut(p):
        if (p < 0.5):
            return 16 * p * p * p * p * p
        else:
            f = ((2 * p) - 2)
            return  0.5 * f * f * f * f * f + 1

    # Modeled after quarter-cycle of sine wave
    def SineEaseIn(p):
        return Easing.sin((p - 1) * Easing.M_PI_2) + 1

    # Modeled after quarter-cycle of sine wave (different phase)
    def SineEaseOut(p):
        return Easing.sin(p * Easing.M_PI_2)

    # Modeled after half sine wave
    def SineEaseInOut(p):
        return 0.5 * (1 - Easing.cos(p * Easing.M_PI))

    # Modeled after shifted quadrant IV of unit circle
    def CircularEaseIn(p):
        return 1 - Easing.sqrt(1 - (p * p))

    # Modeled after shifted quadrant II of unit circle
    def CircularEaseOut(p):
        return Easing.sqrt((2 - p) * p)

    # Modeled after the piecewise circular function
    # y = (1/2)(1 - sqrt(1 - 4x^2))           ; [0, 0.5)
    # y = (1/2)(sqrt(-(2x - 3)*(2x - 1)) + 1) ; [0.5, 1]
    def CircularEaseInOut(p):
        if(p < 0.5):
            return 0.5 * (1 - Easing.sqrt(1 - 4 * (p * p)))
        else:
            return 0.5 * (Easing.sqrt(-((2 * p) - 3) * ((2 * p) - 1)) + 1)

    # Modeled after the exponential function y = 2^(10(x - 1))
    def ExponentialEaseIn(p):
        return p if (p == 0.0) else Easing.pow(2, 10 * (p - 1))

    # Modeled after the exponential function y = -2^(-10x) + 1
    def ExponentialEaseOut(p):
        return p if (p == 1.0) else 1 - Easing.pow(2, -10 * p)

    # Modeled after the piecewise exponential
    # y = (1/2)2^(10(2x - 1))         ; [0,0.5)
    # y = -(1/2)*2^(-10(2x - 1))) + 1 ; [0.5,1]
    def ExponentialEaseInOut(p):
        if(p == 0.0 or p == 1.0):
            return p
        
        if(p < 0.5):
            return 0.5 * Easing.pow(2, (20 * p) - 10)
        else:
            return -0.5 * Easing.pow(2, (-20 * p) + 10) + 1

    # Modeled after the damped sine wave y = sin(13pi/2*x)*pow(2, 10 * (x - 1))
    def ElasticEaseIn(p):
        return Easing.sin(13 * Easing.M_PI_2 * p) * Easing.pow(2, 10 * (p - 1))

    # Modeled after the damped sine wave y = sin(-13pi/2*(x + 1))*pow(2, -10x) + 1
    def ElasticEaseOut(p):
        return Easing.sin(-13 * Easing.M_PI_2 * (p + 1)) * Easing.pow(2, -10 * p) + 1

    # Modeled after the piecewise exponentially-damped sine wave:
    # y = (1/2)*sin(13pi/2*(2*x))*pow(2, 10 * ((2*x) - 1))      ; [0,0.5)
    # y = (1/2)*(sin(-13pi/2*((2x-1)+1))*pow(2,-10(2*x-1)) + 2) ; [0.5, 1]
    def ElasticEaseInOut(p):
        if (p < 0.5):
            return 0.5 * Easing.sin(13 * Easing.M_PI_2 * (2 * p)) * Easing.pow(2, 10 * ((2 * p) - 1))
        else:
            return 0.5 * (Easing.sin(-13 * Easing.M_PI_2 * ((2 * p - 1) + 1)) * Easing.pow(2, -10 * (2 * p - 1)) + 2)

    # Modeled after the overshooting cubic y = x^3-x*sin(x*pi)
    def BackEaseIn(p):
        return p * p * p - p * Easing.sin(p * Easing.M_PI)

    # Modeled after overshooting cubic y = 1-((1-x)^3-(1-x)*sin((1-x)*pi))
    def BackEaseOut(p):
        f = (1 - p)
        return 1 - (f * f * f - f * Easing.sin(f * Easing.M_PI))

    # Modeled after the piecewise overshooting cubic function:
    # y = (1/2)*((2x)^3-(2x)*sin(2*x*pi))           ; [0, 0.5)
    # y = (1/2)*(1-((1-x)^3-(1-x)*sin((1-x)*pi))+1) ; [0.5, 1]
    def BackEaseInOut(p):
        if (p < 0.5):
            f = 2 * p
            return 0.5 * (f * f * f - f * Easing.sin(f * Easing.M_PI))
        else:
            f = (1 - (2*p - 1))
            return 0.5 * (1 - (f * f * f - f * Easing.sin(f * Easing.M_PI))) + 0.5

    def BounceEaseIn(p):
        return 1 - Easing.BounceEaseOut(1 - p)

    def BounceEaseOut(p):
        if(p < 4/11.0):
            return (121 * p * p)/16.0
        
        elif(p < 8/11.0):
            return (363/40.0 * p * p) - (99/10.0 * p) + 17/5.0
        
        elif(p < 9/10.0):
            return (4356/361.0 * p * p) - (35442/1805.0 * p) + 16061/1805.0
        
        else:
            return (54/5.0 * p * p) - (513/25.0 * p) + 268/25.0

    def BounceEaseInOut(p):
        if(p < 0.5):
            return 0.5 * Easing.BounceEaseIn(p*2)
        else:
            return 0.5 * Easing.BounceEaseOut(p * 2 - 1) + 0.5

class FPSMonitor(object):
    from time import time as now

    def __init__(self):
        self.control_time = self.now()
        self.begin_time = self.now()
        self.prev_time = self.begin_time
        self.frames = 0
        self.fps = 0
        self.ms = 0
        self.fps_min = 10
        self.fps_max = 0

        self._doupdate()

    def _doupdate(self):
        self.fps_min = min(self.fps_min, self.fps)
        self.fps_max = max(self.fps_max, self.fps)

        self.text = "%s FPS - %05.2f MS" % (self.fps, self.ms)
        self.markup_text = "<small><tt>%s FPS - %s MS</tt></small>" % (self.fps, self.ms)

    def update(self):
        self.begin_time = self.end()
        return self.text

    def end(self):
        self.frames +=1
        now_time = self.now()
        self.ms = round((now_time - self.begin_time) * 1000, 2)

        if now_time > (self.control_time + 1):
            self.control_time = self.now()
            if self.fps_min == 0 : self.fps_min = self.fps_max

        if now_time > (self.prev_time + 1):
            self.fps = round(self.frames / (now_time - self.prev_time))
            self._doupdate()
            self.prev_time = now_time
            self.frames = 0

        return now_time

    def begin(self):
        self.begin_time = self.now()

class QAudio(object):
    import os, time, ctypes, threading
    import numpy.ctypeslib

    def __init__(self):
        dir_base = self.os.path.dirname(self.os.path.realpath(__file__))
        dir_base += '/qaudio'

        self.qaudio = self.ctypes.CDLL("%s/%s" % (dir_base, 'libqaudio.so'))
        self.running = False
    
    def __del__(self):
        self.close()

    def is_open(self):
        return True if self.qaudio.is_open() else False


    def open(self, buffer_size = 1024, channels = 2):
        self.qaudio.read_stream.restype = self.numpy.ctypeslib.ndpointer(dtype=(self.ctypes.c_int), shape=(buffer_size, ))

        self.qaudio.open_stream(buffer_size, channels)
    
    def read(self):
        return self.qaudio.read_stream()

    def close(self):
        if(self.qaudio.is_open()): self.qaudio.close_stream()


    def open_async(self, buffer_size = 1024, channels = 2, callback = None, start = False):
        self.open(buffer_size=buffer_size, channels=channels)
        # self.time.sleep(2)

        # print("Is Open:", self.is_open())

        def thread_main ():
            while self.is_open():
                # self.time.sleep(0.01)
                if(callback != None): callback(self.read())
            
            # print("Thread end")
                

        self.async_thread = self.threading.Thread(target=thread_main, daemon=True)
        
        if start: self.start_async()
        
    def start_async(self):
           self.async_thread.start() 

class SoundBars(object):
    import math 
    import numpy as np
    import gi, time, cairo
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GLib
    from collections import deque
    from scipy import signal
    
    css = """
        .bars {
            background: rgba(83, 0, 0, 0.0);
            padding: 0;
        }
        .bars .area {
            background-color: blue;
            padding:10px;
        }
        .lixo {   
            transition: all 200ms ease-in-out;           
        }
        .fps {
            font-weight: bold;
            color: rgba(66, 253, 57, 1);
            text-shadow: 0px 0px 1px rgba(0, 0, 0, 1);
        }
    """

    rate = 44100
    buffer_size = 1024

    last_max = -math.inf

    data_buffer_size = 32
    last_read_time = 0
    
    normalization_array = None    

    stream_new_data = False

    def __init__(self, bars=100, fps=60, width=800, height=400, show_fps=False, mirror=False, space=2, opacity=0.9):
        self.bar_qt = bars
        self.fps = fps
        self.width = width
        self.height = height
        self.mirror = mirror
        self.show_fps = show_fps
        self.spacing = space
        self.opacity = opacity


        self.last_fft = [0.0] * int(self.bar_qt / 2)
        self.curr_fft = [0.0] * int(self.bar_qt / 2)
        self.curr_fft_slower = [0.0] * int(self.bar_qt / 2)

        self.data_buffer = self.deque(maxlen=self.data_buffer_size)


        self.container = self.Gtk.Box()
        self.FPS = FPSMonitor()

        self.qaudio = None

    def _create(self):
        container = self.Gtk.Grid()
        container.get_style_context().add_class('bars')
        container.set_size_request(-1, self.height)
        container.set_valign(self.Gtk.Align.END)
        container.set_halign(self.Gtk.Align.CENTER)
        container.set_column_spacing(self.spacing)
        container.set_row_spacing(0)
        # container.set_column_homogeneous(True)
        # container.set_row_homogeneous(True)
        self.container = container

        self.bar_width = (self.width / self.bar_qt)
        # bar_width = 10

        # qprint( self.bar_width, (self.bar_width * self.bar_qt) )

        # Create Style

        style_provider = self.Gtk.CssProvider()
        style_provider.load_from_data(self.css.encode('utf-8'))
        container.get_style_context().add_provider_for_screen(container.get_screen(), style_provider, self.Gtk.STYLE_PROVIDER_PRIORITY_USER)


        self.darea = self.Gtk.DrawingArea()
        self.darea.set_size_request(self.width, self.height)
        self.darea.get_style_context().add_class('area')
        self.darea.set_margin_start(0)
        self.darea.set_margin_end(0)
        self.darea.set_margin_top(0)
        self.darea.set_margin_bottom(0)
        self.darea.set_halign(self.Gtk.Align.CENTER)
        self.darea.connect("draw", self.on_draw)
        self.container.add(self.darea)



    def now(self): return self.time.time() * 1000.0


    # Drawing Functions

    def rgb_normalized(self, r, g, b):
        if r == 0: r = 1
        if g == 0: g = 1
        if b == 0: b = 1
        rgb = {
            'r' : r / (255/1.0) ,
            'g' : g / (255/1.0) ,
            'b' : b / (255/1.0)
        }

        return rgb
    

    def _draw_bars(self, widget, cr, fft, fft_slower):
        space = self.spacing / 2
        border = self.spacing / 2
        line_w = self.bar_width - space

        thing_size = self.height * 0.01

        cr.set_line_width(border)
        
        c_from = {
            'r' : 0.801600 ,
            'g' : 0.158400 ,
            'b' : 0.587200 
        }

        c_to = {
            'r' : 0.960784 ,
            'g' : 0.266667 ,
            'b' : 0.431373 
        }

        c_from = self.rgb_normalized(204, 40 ,149)
        # c_from = self.rgb_normalized(253, 76 ,122)
        # c_from = self.rgb_normalized(252, 76 ,117)
        # c_to = self.rgb_normalized(253, 216, 59)

        # c_from = self.rgb_normalized(253, 254 ,198)
        c_to = self.rgb_normalized(255, 208, 65)
       

        height = self.height
        width = (self.width ) / 2 - space 
       
        index = 0;
        for n in range(len(fft)):            
            v = fft[n] + 0.01
            v_slow = fft_slower[n] + 0.01
            
            ni = len(fft) - n

            ease = Easing.QuinticEaseOut(min(1, v))

            # color = (80/255 / len(fft)*2)

            # if(n > len(fft)/2): color = color * (n + 1)
            # else: color = color * ni


            # c_from['b'] = color
            # c_to['b'] = color

            r = self._lerp(c_from['r'], c_to['r'], ease)
            g = self._lerp(c_from['g'], c_to['g'], ease)
            b = self._lerp(c_from['b'], c_to['b'], ease)
            
            cr.set_source_rgba(r, g, b, self.opacity)
            

            if(not self.mirror):
                cr.rectangle(index + space/2,  height - (height * v), line_w, height)
                index += space

                cr.fill_preserve()
                cr.set_source_rgba(0, 0, 0, self.opacity /2)
                cr.stroke()
                
                index -= space
                cr.set_source_rgba(0.997333, 0.850119, 0.982568, self.opacity)
                cr.rectangle(index + space/2,  height - (height * v_slow) - thing_size, line_w, thing_size)
                index += space

                cr.fill()
            else:
                cr.rectangle(index - line_w + space/2,  ( height / 2 - (height / 2 * v)) , line_w, (height  * v))
                index += space
                cr.rectangle(index + space/2,  ( height / 2 - (height / 2 * v)) , line_w, (height  * v) )

            
                cr.fill_preserve()
                cr.set_source_rgba(0, 0, 0, self.opacity /2)
                cr.stroke()

            index += line_w


    def _draw_bg(self, widget, cr):
        allo = widget.get_allocation()
        w, h = (allo.width, allo.height)

        cr.set_source_rgba(0.1, 0.1, 0.1, 0.7)
        cr.rectangle(0,0, w, h)
        cr.fill()

    def _draw_fps(self, widget, cr):
        text = self.FPS.update()
        
        cr.select_font_face("Monospace", self.cairo.FONT_SLANT_NORMAL, self.cairo.FONT_WEIGHT_BOLD)
        cr.set_font_size(13)
        
        allo = widget.get_allocation()
        width, height = (allo.width, allo.height)

        margin = 5

        (x, y, w, h, dx, dy) = cr.text_extents(text)
        

        cr.set_source_rgba(0, 0, 0, 0.8)
        cr.rectangle(width/2 - w/2 - margin, 0, w + margin*2, h + margin*2)
        cr.fill()

        # print(x, y, "-",  w, h, "-",  dx, dy)

        # cr.set_source_rgba(0.0, 0.0, 0.0, 1)
        # cr.move_to(width/2 - w/2 + 1, h + margin + 1)    
        # cr.show_text(text)

        cr.set_source_rgba(0.5, 0.9, 0.5, 0.9)
        cr.move_to(width/2 - w/2, h + margin)    
        cr.show_text(text)
        


    def on_draw(self, widget, cr):

        time_delta = (self.now() - self.last_update)


        # self._draw_bg(widget, cr)

       
        # self.curr_fft = temp
        # self.curr_fft_slower = temp

        t =  0.4
        self.curr_fft = self._lerp_arr(self.curr_fft, self.last_fft, Easing.LinearInterpolation(t))
        self.curr_fft_slower = self._lerp_arr3(self.curr_fft_slower, self.curr_fft, Easing.LinearInterpolation(t))

        

        temp_fft = [*reversed(self.curr_fft), * self.curr_fft]
        temp_fft_slow = [*reversed(self.curr_fft_slower), * self.curr_fft_slower]
 

        # print(len(self.curr_fft), self.np.average(self.curr_fft) < 0.001)
 
        # if self.curr_fft is not None or self.np.average(self.curr_fft) > 0.001:
        self._draw_bars(widget, cr, temp_fft, temp_fft_slow)


        if(self.show_fps): self._draw_fps(widget, cr)

        self.last_update = self.now()

        return False
            

    def _get_fft(self):
        shift = 2
        trim = int(self.bar_qt/2)
        read_delta = (self.now() - self.last_read_time)

        success = False
        if self.stream_new_data:
            try:            
                data = self.data_buffer.pop()

                # data = data * self.np.hanning(len(data))
                fft = self.np.abs(self.np.fft.rfft(data, norm="ortho")[1:])
                fft_len = len(fft)
                
                # self.last_max = max(self.last_max, max(fft))
                # print(self.last_max)

                if(self.normalization_array == None):
                    normalization_array = self.np.linspace(1, fft_len/2, int(fft_len * 2.5))


                fft_cropped = fft[:trim + shift] 
                
                for i in range(len(fft_cropped)):
                    # fft_cropped[i] = fft_cropped[i] * (1.0 / fft_len) / fft_len
                    fft_cropped[i] = fft_cropped[i] * (1.0 / fft_len) / fft_len * normalization_array[i]
                    fft_cropped[i] = max(0, min(0.95, fft_cropped[i]))

                fft_cropped = self._lowpass_filter(fft_cropped, cutoff=3.1, order=1)

                fft_cropped = fft_cropped[shift:] 

        
                self.last_fft = fft_cropped
                self.last_read_time = self.now()
                self.stream_new_data = False
                success = True

            except Exception as e: qprint("SoundBars", "_get_fft ERROR", e) 

        return success, read_delta 

    def _process(self):
        fps_delta = (1000/self.fps)

        time_delta = (self.now() - self.last_update)
        

        success, read_delta = self._get_fft()
    
        if success:
            self.darea.queue_draw()


        self.GLib.timeout_add(fps_delta, self._process)
        


    # Helpers    
    def _lerp_arr(self, a1, a2, t):
        for i in range(len(a1)):
            a1[i] = max(0.001, (a1[i] + (a2[i] - a1[i]) * t))
        return a1 
    
    def _lerp_arr3(self, a1, a2, t):
        for i in range(len(a1)):
            v = t
            v = Easing.CubicEaseOut( (a2[i] * 0.05) + 0.01 )
            # print(curr)
            
            if(a1[i] <= a2[i]):
                a1[i] = a2[i]
            else:
                a1[i] = (a1[i] + (a2[i] - a1[i]) * v)
                pass

        return a1 


    def _lerp(self, a1, a2, t):
        a1 = (a1 + (a2 - a1) * t)
        return a1 




    def _lowpass_filter(self, fft, cutoff=3.1, fs=30.0, order=2):
        b, a = self.signal.butter(order, cutoff, btype='low', fs=fs)
        return self.signal.lfilter(b, a, fft)


    def _init(self):
        def on_data(data):
            self.data_buffer.append(data)
            self.stream_new_data = True

            # print(max(data[256:]))
            # self.GLib.timeout_add(10, self._process)
            # self._process()
            self.time.sleep(0.01)
            # self.time.sleep((1/self.fps))

        try:
            self.qaudio = QAudio()
            self.qaudio.open_async(buffer_size=self.buffer_size, channels=2, callback=on_data)

            self.qaudio.start_async()


            self.last_update = self.now()
            self.last_update2 = self.now() 

            self._process()
                
        except Exception as e:
            qprint("SoundBars", "Start ERROR", e)


    def close(self):
        if(self.qaudio): self.qaudio.close()


    def start(self):
        self._create()
        self._init()


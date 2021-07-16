#!/usr/bin/python3

import gi, cairo, argparse
gi.require_version('Gtk', '3.0')
# gi.require_version('GLib', '2.0')
# gi.require_version('Gst', '1.0')
# gi.require_version('GstVideo', '1.0')
from gi.repository import Gtk, Gdk
from QTools import SoundBars


class SoundWindow(Gtk.Window):
    css = """
            window {                
                background: rgba(0, 0, 0, 0.9);
            }
            window   {                
                border-radius: 0px;
                margin: 0px;
                background: rgba(127, 47, 116, 0.0);
                background: rgba(44, 49, 58, 0.0);
                box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0.0);
                border: 0px solid black;
                padding: 0px;
            }
        """

    def __init__(self, width=900, height=400, show_fps=False, max_fps=40, bars=80, mirror=True, space=1, opacity=0.7):
        Gtk.Window.__init__(self, title="Sound Bars")

        # Default Values
        self.set_default_size(width, height)
        self.set_decorated(False)
        self.set_resizable(True)
        self.set_border_width(0)
        self.set_position(Gtk.WindowPosition.CENTER)
        # self.set_keep_above(True)
        # self.set_keep_below(True)


        # Set Transparency
        self.set_visual(self.get_screen().get_rgba_visual())

        # Load CSS
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(self.css.encode('utf-8'))
        self.get_style_context().add_provider_for_screen(self.get_screen(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

        # Bind Events
        self.connect("destroy", self._on_close)
        self.connect("button-press-event", self.on_button_press)
        self.connect("key-release-event", self.on_key_release)

        # Main Widgets

        base = Gtk.Grid()
        base.set_valign(Gtk.Align.FILL)
        base.set_halign(Gtk.Align.FILL)
        # self.add(base)

        overlay = Gtk.Overlay()
        overlay.set_valign(Gtk.Align.FILL)
        overlay.set_halign(Gtk.Align.FILL)
        overlay.add(Gtk.Box())

        self.add(overlay)

        # self.video = VideoLoop("neon.mp4")
        # self.add(self.video.get_widget())

        self.SB = SoundBars(bars=bars, fps=max_fps, width=width, height=height, show_fps=show_fps, mirror=mirror, space=space, opacity=opacity)
        self.SB.start()


        overlay.add_overlay(self.SB.container)



        # thread = threading.Thread(target=self.example_target)
        # thread.daemon = True
        # thread.start()
        # thread.join()

        self.show_all()


    def _on_close(self, widget = None):
        try: self.SB.close()
        except: pass

        Gtk.main_quit()

    def on_button_press(self, widget, ev):
        if ev.button in (1,3):
            self.begin_move_drag(ev.button, ev.x_root, ev.y_root, ev.time)
        return True

    def on_key_release(self, widget, ev, data=None):
        if ev.keyval == (Gdk.KEY_Escape):
            self._on_close()
        if ev.keyval == (Gdk.KEY_space):
            pass
        return True


parser = argparse.ArgumentParser()
parser.add_argument('--size', type=str, default="1000x300", dest='size', help='Window Size (default: 1600x900) ')
parser.add_argument('--max_fps', '--max-fps', type=int, default=60, dest='max_fps', help='Max FPS')
parser.add_argument('--bars', type=int, default=80, dest='bars', help='Number of bars')
parser.add_argument('--space', type=int, default=2, dest='space', help='Space Between Bars')
parser.add_argument('--opacity', type=float, default=0.8, dest='opacity', help='Overall Opacity')
parser.add_argument('--fps', '--fps_show', action=argparse._StoreTrueAction, dest='fps_show', help='Show FPS')
parser.add_argument('--no_mirror', '--no-mirror', action=argparse._StoreFalseAction, dest='mirror', help='Remove Mirror Effect')
args = parser.parse_args()

w, h = (900, 300)

try:
    w, h = args.size.split('x')
except: pass

# print(args)




win = SoundWindow(width=int(w), height=int(h), show_fps=args.fps_show, max_fps=args.max_fps, mirror=args.mirror, bars=args.bars, space=args.space, opacity=args.opacity)
# win.show_all()
Gtk.main()
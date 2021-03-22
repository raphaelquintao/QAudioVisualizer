QAudioVisualizer
===
Non GPU and Low CPU usage GTK Audio Visualizer

![Demo2](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/demo2.gif)

![Demo1](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/demo1.gif)

Demo no Mirror:
[mp4](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/demo2.mp4)
[flv](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/demo2.flv)

Demo Mirror:
[mp4](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/demo1.mp4)


## Requirements

### C

- Pulse Audio (libpulse)
    - Debian: `sudo apt-get install lippulse0 libpulse-dev`
    
### Python

- Python 3
- Numpy (numpy)
    - `pip3 install numpy`
- SciPy (scipy)
    - `pip3 install scipy`

## Compiling C Library

 - Compiling c library
    
    `cd qaudio`\
    `make`


## Usage

`soundbars.py [-h] [--size SIZE] [--max_fps MAX_FPS] [--bars BARS] [--space SPACE] [--opacity OPACITY] [--fps] [--no_mirror]`


Parameter | Description 
----------|------------
-h, --help | show this help message and exit
--size | Window Size (default: 1600x900)
--max_fps | Max FPS
--bars | Number of bars
--space | Space Between Bars (default: 1)
--opacity | Overall Opacity (default: 0.7)
--fps, --fps_show | Show FPS
--no_mirror | Remove Mirror Effect

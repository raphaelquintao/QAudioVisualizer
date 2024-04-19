QAudioVisualizer
===
Non GPU and Low CPU usage GTK Audio Visualizer

|Normal|Mirror|
|---|---|
![normal](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/normal.gif) | ![mirror](https://raw.githubusercontent.com/raphaelquintao/QAudioVisualizer/master/demo/mirror.gif)

https://github.com/raphaelquintao/QAudioVisualizer/assets/2568375/dc5d93a0-fa54-4f89-a7a7-d83b20de9e27

https://github.com/raphaelquintao/QAudioVisualizer/assets/2568375/94d4e1f4-59a8-4412-a744-bddc8e6d1a6d


## How it works

1. Basically you need to get the raw output from the sound card (C does that very well). 
2. Run a [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
3. Then a [Low-pass filter](https://en.wikipedia.org/wiki/Low-pass_filter)
4. Finally, some [Linear interpolation](https://en.wikipedia.org/wiki/Linear_interpolation) to draw

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

`cd qaudio` \
`make`


## Usage

`./soundbars.py [-h] [--size SIZE] [--max_fps MAX_FPS] [--bars BARS] [--space SPACE] [--opacity OPACITY] [--fps] [--no_mirror]`


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

**Real-Time Audio Spectrum Analyzer (FFT)**

This project is a real-time audio spectrum analyzer built in Python using the Fast Fourier Transform (FFT).

It captures audio from the microphone, computes the frequency spectrum in real time, and visualizes:

A smoothed FFT spectrum (0–5 kHz)

Log-scale magnitude (cleaner + more readable)

Real-time peak frequency detection

Separate Bass / Mid / Treble band levels with live bar meters

I built this as a freshman Electrical & Computer Engineering student to learn practical digital signal processing, Fourier transforms, and real-time data visualization.

**Features**

Live microphone audio input

Real-time FFT using numpy.fft.rfft

Blackman windowing to reduce spectral leakage

Exponential smoothing for clean visuals (less jitter)

Log-magnitude scaling (like professional audio analyzers)

Band energy bars:

Bass: 20–250 Hz

Mid: 250–2000 Hz

Treble: 2000–5000 Hz

Real-time peak frequency readout displayed in the window title

Built using matplotlib for dynamic live plotting

**How It Works**

Microphone samples are captured at a fixed sample rate (44.1 kHz).

Audio is divided into blocks of block_size samples.

Each audio block is multiplied by a window function (Blackman) to reduce artifacts.

The FFT is computed:

X[k]=n=0∑N−1​x[n]e−j2πnk/N

Magnitudes are:

Smoothed over time (exponential moving average)

Converted to log scale so quieter frequencies are visible

Frequency bins are classified into Bass, Mid, and Treble bands.

A live graph updates:

The FFT curve (spectrum)

A bar chart of the band energy levels

The dominant frequency is displayed in real time.

**Tech Stack**

Language: Python 3.10
Libraries used:

numpy — FFT + numerical computing

sounddevice — microphone input

matplotlib — real-time plotting

(optional) scipy for filters or spectrograms later

**Getting Started**
*Install Dependencies*

Make sure you are using Python 3.10 or similar. Then install:

pip install numpy matplotlib sounddevice


(If using PyCharm, install these in your project interpreter.)

*Run the Analyzer*
python realtime_fft.py


A window will open showing:

Live FFT spectrum

Bass/Mid/Treble meters

Peak frequency in Hz

Talk, clap, whistle, or play music — the analyzer reacts instantly.

**Tunable Parameters**

Inside realtime_fft.py, you can adjust:

*Sample rate*
sample_rate = 44100

*FFT block size*
block_size = 1024


Smaller = more responsive,
Larger = smoother but slower.

*Smoothing factor*
alpha = 0.4


0.1 → very smooth

0.8 → very reactive

*Band definitions*
bands = [
    ("Bass",   20,   250),
    ("Mid",    250,  2000),
    ("Treble", 2000, 5000),
]


**What I Learned**

Through this project, I gained experience in:

Real-time audio processing

Using FFT to transform signals to the frequency domain

Windowing techniques (Blackman/Hann)

Smoothing and visualization filtering

Frequency band analysis (bass/mid/treble separation)

Real-time graphing in Python

Understanding microphone input streams

**Future Improvements**

Add a spectrogram view (heatmap over time)

Analyze .wav files instead of live mic

Add filters (low-pass, high-pass, band-pass)

Log band levels to CSV for plotting later

Package the analyzer into a GUI app

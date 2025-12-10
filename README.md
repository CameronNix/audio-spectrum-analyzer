# 🎧 Real-Time Audio Spectrum Analyzer (FFT)

This project is a **real-time audio spectrum analyzer** built in Python using the **Fast Fourier Transform (FFT)**.

It captures audio from the **microphone**, computes the frequency spectrum in real time, and visualizes:

- A smoothed **FFT spectrum** (0–5 kHz)
- **Log-scale magnitude** for clean readability
- Real-time **peak frequency detection**
- Separate **Bass / Mid / Treble** band levels using live bar meters

I built this project to explore practical **digital signal processing**, **Fourier transforms**, and **real-time data visualization**.

---

## 🔍 Features

- 🎙️ **Live microphone audio input**
- ⚡ Real-time **FFT** using `numpy.fft.rfft`
- 🪟 **Blackman windowing** to reduce spectral leakage
- 📉 **Exponential smoothing** for clean, stable visuals
- 📈 **Log-magnitude scaling** (used in professional analyzers)
- 🎚️ **Band energy bars**:
  - **Bass:** 20–250 Hz  
  - **Mid:** 250–2000 Hz  
  - **Treble:** 2000–5000 Hz  
- 🎯 Real-time **peak frequency detection** displayed in the window title
- 📊 Dynamic visualization with `matplotlib`

---

## 🧠 How It Works

1. Microphone audio is sampled at a fixed **sample rate** (44.1 kHz).
2. Samples are grouped into blocks defined by `block_size`.
3. Each block is multiplied by a **Blackman window** to reduce edge artifacts.
4. The **FFT** converts the time-domain samples into frequency bins.
5. Magnitudes are:
   - Smoothed using an exponential moving average  
   - Converted to **log scale** to reveal quiet frequencies
6. Frequencies are grouped into **Bass**, **Mid**, and **Treble** bands.
7. The spectrum curve and band-level bars update continuously in real time.
8. The highest-energy frequency bin is labeled as the **peak frequency**.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10  
- **Libraries:**
  - `numpy` — FFT and numerical processing  
  - `sounddevice` — real-time microphone capture  
  - `matplotlib` — live plotting  

---

## 🚀 Getting Started

### 1. Install Dependencies

    pip install numpy matplotlib sounddevice

Use Python 3.10 or similar for best compatibility.

### 2. Run the Analyzer

    python realtime_fft.py

The window will show:

- A real-time FFT spectrum  
- Three band meters (Bass / Mid / Treble)  
- A live peak frequency (Hz)

Speak, clap, whistle, or play music — the analyzer reacts instantly.

---

## 🎛️ Tunable Parameters

### Sample Rate
    sample_rate = 44100

### FFT Block Size
    block_size = 1024

- Smaller = faster response  
- Larger = better frequency detail  

### Smoothing Factor
    alpha = 0.4

- 0.1 → very smooth  
- 0.8 → very reactive  

### Frequency Bands
    bands = [
        ("Bass",   20,   250),
        ("Mid",    250,  2000),
        ("Treble", 2000, 5000),
    ]

---

## 🧾 What I Learned

- How to capture and process real-time audio streams  
- How the FFT converts signals from time-domain to frequency-domain  
- Why Blackman and Hann windows improve spectral accuracy  
- How to compute and visualize band energy levels  
- How smoothing and log-scaling improve real-time displays  
- Techniques for building dynamic visualizations in Python  

---

## 🔮 Future Improvements

- Spectrogram mode (frequency vs time heatmap)  
- WAV-file analysis instead of microphone-only input  
- Basic digital filters (low-pass, high-pass, band-pass)  
- Option to record data and export for plotting  
- GUI controls for selecting device, sample rate, etc.  

---

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# ---------- Settings ----------
sample_rate = 44100        # samples per second
block_size = 1024          # samples per FFT frame

# ---------- Globals ----------
latest_fft = np.zeros(block_size // 2 + 1)
smoothed_fft = np.zeros(block_size // 2 + 1)
alpha = 0.4                 # 0.1 = super smooth, 0.8 = more reactive
latest_peak_freq = 0.0      # Hz

# ---------- Frequency bins ----------
freqs = np.fft.rfftfreq(block_size, 1 / sample_rate)

# Define bands (in Hz)
bands = [
    ("Bass",   20,   250),
    ("Mid",    250,  2000),
    ("Treble", 2000, 5000),
]

# Precompute masks for each band
band_masks = []
for _, f_low, f_high in bands:
    mask = (freqs >= f_low) & (freqs < f_high)
    band_masks.append(mask)

band_levels = np.zeros(len(bands))

# ---------- Plot setup ----------
plt.ion()
fig, (ax_spec, ax_bar) = plt.subplots(
    2, 1, figsize=(8, 6), gridspec_kw={"height_ratios": [3, 1]}
)

# Spectrum line
line, = ax_spec.plot(freqs, np.zeros_like(freqs))
ax_spec.set_xlim(0, 5000)   # focus on 0–5 kHz
ax_spec.set_ylim(0, 50)
ax_spec.set_xlabel("Frequency (Hz)")
ax_spec.set_ylabel("Log Magnitude")
ax_spec.set_title("Real-Time FFT Audio Spectrum")

# Band bars
band_names = [b[0] for b in bands]
x_pos = np.arange(len(bands))
bars = ax_bar.bar(x_pos, np.zeros(len(bands)))
ax_bar.set_xticks(x_pos)
ax_bar.set_xticklabels(band_names)
ax_bar.set_ylabel("Band Level")
ax_bar.set_ylim(0, 50)

plt.tight_layout()

# ---------- Audio callback ----------
def audio_callback(indata, frames, time, status):
    global latest_fft, latest_peak_freq

    if status:
        print(status)

    # Take first channel
    audio_data = indata[:, 0]

    # Windowing to clean up the spectrum (Blackman window)
    window = np.blackman(len(audio_data))
    audio_data = audio_data * window

    # FFT magnitude
    fft_vals = np.abs(np.fft.rfft(audio_data))
    latest_fft = fft_vals

    # Dominant frequency (peak bin)
    peak_idx = np.argmax(fft_vals)
    latest_peak_freq = freqs[peak_idx]


# ---------- Audio stream ----------
stream = sd.InputStream(
    callback=audio_callback,
    channels=1,
    samplerate=sample_rate,
    blocksize=block_size
)

# ---------- Main loop ----------
with stream:
    while plt.fignum_exists(fig.number):
        # Exponential smoothing on FFT
        smoothed_fft[:] = alpha * smoothed_fft + (1 - alpha) * latest_fft

        # Log scale so small values show up
        log_fft = np.log1p(smoothed_fft) * 10

        # Update spectrum line
        line.set_ydata(log_fft)
        ax_spec.set_ylim(0, max(10, log_fft.max() * 1.2))
        ax_spec.set_title(
            f"Real-Time FFT Audio Spectrum  |  Peak: {latest_peak_freq:6.1f} Hz"
        )

        # ----- Update band levels -----
        for i, mask in enumerate(band_masks):
            if mask.any():
                # Use mean energy in the band, then log-scale it
                level = smoothed_fft[mask].mean()
                band_levels[i] = np.log1p(level) * 10
            else:
                band_levels[i] = 0.0

        # Update bar heights
        for bar, lvl in zip(bars, band_levels):
            bar.set_height(lvl)

        ax_bar.set_ylim(0, max(10, band_levels.max() * 1.2))

        plt.pause(0.01)

print("Stream closed, exiting.")



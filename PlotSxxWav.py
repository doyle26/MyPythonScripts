import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import welch

# Replace 'your_audio.wav' with the path to your WAV file
wav_file = 'pink_noise_amplitude.wav'

# Read the WAV file
sample_rate, audio_data = wavfile.read(wav_file)

# Calculate the single-sided spectral density
frequencies, density = welch(audio_data, fs=sample_rate, nperseg=1024)

# Plot the single-sided spectral density
plt.figure(101,figsize=(10, 6))
plt.loglog(frequencies, density)
plt.title('Single-Sided Spectral Density')
plt.xlabel('Frequency (Hz) [log scale]')
plt.ylabel('Spectral Density (Power/Frequency)')
plt.grid(True)
plt.show()

#user_input = input("Press Enter to exit the script...")

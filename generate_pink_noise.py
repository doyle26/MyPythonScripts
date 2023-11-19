import numpy as np
import scipy.io.wavfile as wavfile

def pink_noise(length, sample_rate, amplitude=0.5, seed=None):
    if seed is not None:
        np.random.seed(seed)

    # The number of octaves in the pink noise
    num_octaves = int(np.log2(length))

    # Generate white noise
    white_noise = np.random.normal(0, 1, length)

    # Compute the power spectral density of the white noise
    fft_data = np.fft.fft(white_noise)
    psd = np.abs(fft_data)**2

    # Apply the 1/f filter to the power spectral density
    for i in range(1, num_octaves):
        psd /= np.abs(np.fft.fft(np.arange(0, length)))

    # Inverse FFT to obtain the pink noise
    pink_noise = np.fft.ifft(np.sqrt(psd)).real

    # Normalize the pink noise to have a standard deviation of 1
    pink_noise /= np.std(pink_noise)

    # Scale the pink noise by the specified amplitude
    pink_noise *= amplitude

    return pink_noise

# Parameters
duration_seconds = 10  # Duration of the pink noise in seconds
sample_rate = 44100  # Sample rate in Hz
amplitude = 0.5  # Amplitude control (adjust as needed)
output_filename = "pink_noise_amplitude.wav"

# Calculate the length of the pink noise based on duration and sample rate
length = duration_seconds * sample_rate

# Generate pink noise with the specified amplitude
pink = pink_noise(length, sample_rate, amplitude=amplitude, seed=42)

# Save pink noise as a WAV file
wavfile.write(output_filename, sample_rate, pink)

print(f"Saved pink noise to {output_filename} with amplitude {amplitude}")

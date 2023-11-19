# Parameters
duration_seconds = 10  # Duration of the pink noise in seconds
sample_rate = 48000  # Sample rate in Hz
amplitude = 0.71  # Amplitude control
output_filename = "test_file.wav"

# Calculate the length of the pink noise based on duration and sample rate
length = duration_seconds * sample_rate

# Generate pink noise with the specified amplitude
pink = pink_noise(length, sample_rate, amplitude=amplitude, seed=42)

# Save pink noise as a WAV file
wavfile.write(output_filename, sample_rate, pink)

print(f"Saved pink noise to {output_filename} with amplitude {amplitude}")

import pyaudio
import numpy as np
from scipy.signal import butter, lfilter

##def apply_filter(data, b, a):
##    # Apply digital filter using lfilter
##    return lfilter(b, a, data)

def apply_equalizer(data, eq_gain):
    eq_gain_reshaped = eq_gain[:, np.newaxis]
    return lfilter(b, a, data)#data * eq_gain_reshaped

def design_lowpass_filter(cutoff_freq, fs, order=4):
    # Design a low-pass Butterworth filter
    nyquist = 0.5 * fs
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def main():
    chunk_size = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()

    stream = p.open(
        format=sample_format,
        channels=channels,
        rate=rate,
        input=True,
        output=True,
        frames_per_buffer=chunk_size
    )

    print("Equalizer script is running. Press Ctrl+C to exit.")

    # Design a low-pass filter with a cutoff frequency of 1000 Hz
    cutoff_frequency = 4000.0
    filter_order = 4
    b, a = design_lowpass_filter(cutoff_frequency, rate, filter_order)


    try:
        while True:
            try:
                input_data = stream.read(chunk_size)
                input_array = np.frombuffer(input_data, dtype=np.int16)
                equalizer_gain = np.array([1.0])  # Adjust the gain values based on your requirements
                output_array = apply_equalizer(input_array, equalizer_gain)
                output_data = output_array.astype(np.int16).tobytes()
                stream.write(output_data)
            except IOError as e:
                # Ignore "Input overflowed" errors
                if e.errno != pyaudio.paInputOverflowed:
                    raise

    except KeyboardInterrupt:
        print("Exiting...")

    finally:
        # Stop and close the stream and PyAudio
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()

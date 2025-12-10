"""
Visualization utilities for audio data.

Functions to plot audio waveforms, spectrograms, frequency spectra,
and comparisons using matplotlib and Streamlit.
"""

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import librosa
import librosa.display


def plot_audio_waveform(audio_data, sample_rate, title='Audio Waveform'):
    """
    Plot the waveform of an audio signal.

    Args:
        audio_data (np.ndarray): Audio signal data.
        sample_rate (int): Sampling rate of the audio.
        title (str): Title of the plot.
    """
    fig, ax = plt.subplots(figsize=(10, 3))

    times = np.arange(len(audio_data)) / sample_rate

    ax.plot(times, audio_data, linewidth=0.5)

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)

    st.pyplot(fig)
    plt.close()


def plot_spectrogram(audio_data, sample_rate, title='Spectrogram'):
    """
    Plot the spectrogram of an audio signal.

    Args:
        audio_data (np.ndarray): Audio signal data.
        sample_rate (int): Sampling rate of the audio.
        title (str): Title of the plot.
    """
    fig, ax = plt.subplots(figsize=(10, 4))

    spectrogram_db = librosa.amplitude_to_db(
        np.abs(librosa.stft(audio_data)), ref=np.max
    )

    img = librosa.display.specshow(
        spectrogram_db,
        x_axis='time',
        y_axis='hz',
        sr=sample_rate,
        ax=ax,
    )

    ax.set_title(title)

    fig.colorbar(img, ax=ax, format='%+2.0f dB')

    st.pyplot(fig)
    plt.close()


def plot_frequency_spectrum(audio_data, sample_rate, title='Frequency Spectrum'):
    """
    Plot the frequency spectrum of an audio signal.

    Args:
        audio_data (np.ndarray): Audio signal data.
        sample_rate (int): Sampling rate of the audio.
        title (str): Title of the plot.
    """
    fig, ax = plt.subplots(figsize=(10, 4))

    # Calculate FFT
    n_fft = min(8192, len(audio_data))
    fft = np.fft.fft(audio_data, n_fft)
    freqs = np.fft.fftfreq(n_fft, 1/sample_rate)

    # Positive frequencies
    positive_freq_idx = freqs >= 0
    freqs_positive = freqs[positive_freq_idx]
    magnitude = np.abs(fft[positive_freq_idx])

    ax.plot(freqs_positive, magnitude, linewidth=1)
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel('Magnitude')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, sample_rate/2)

    st.pyplot(fig)
    plt.close()


def plot_comparison(original_data, processed_data, sample_rate, effect_name):
    """
    Plot original and processed audio waveforms side by side with effect name.
    """
    col1, col2 = st.columns(2)

    with col1:
        plot_audio_waveform(
            original_data, sample_rate,
            f'Original Waveform – {effect_name}'
        )

    with col2:
        plot_audio_waveform(
            processed_data, sample_rate,
            f'Processed Waveform – {effect_name}'
        )


def plot_spectrogram_comparison(original_data, processed_data, sample_rate,
                               effect_name):
    """
    Plot original and processed audio spectrograms side by side with effect name.
    """
    col1, col2 = st.columns(2)

    with col1:
        plot_spectrogram(
            original_data, sample_rate,
            f'Original Spectrogram – {effect_name}'
        )

    with col2:
        plot_spectrogram(
            processed_data, sample_rate,
            f'Processed Spectrogram – {effect_name}'
        )


def plot_frequency_spectrum_comparison(original_data, processed_data,
                                      sample_rate, effect_name):
    """
    Plot original and processed audio frequency spectra side by side with effect name.
    """
    col1, col2 = st.columns(2)

    with col1:
        plot_frequency_spectrum(
            original_data, sample_rate,
            f'Original Spectrum – {effect_name}'
        )

    with col2:
        plot_frequency_spectrum(
            processed_data, sample_rate,
            f'Processed Spectrum – {effect_name}'
        )


def plot_comprehensive_comparison(original_data, processed_data, sample_rate,
                                 transformation_name):
    """
    Plot comprehensive comparison including waveforms, spectrograms
    and frequency spectra.

    Args:
        original_data (np.ndarray): Original audio data.
        processed_data (np.ndarray): Processed audio data.
        sample_rate (int): Sampling rate of the audio.
        transformation_name (str): Name of the transformation applied.
    """
    st.header(f"Analysis: {transformation_name}")

    # Waveform comparison
    st.subheader("Waveform Comparison")
    plot_comparison(original_data, processed_data, sample_rate,
                   transformation_name)

    # Frequency spectrum comparison
    st.subheader("Frequency Spectrum Comparison")
    plot_frequency_spectrum_comparison(original_data, processed_data,
                                      sample_rate, transformation_name)

    # Spectrogram comparison
    st.subheader("Spectrogram Comparison")
    plot_spectrogram_comparison(original_data, processed_data, sample_rate,
                               transformation_name)

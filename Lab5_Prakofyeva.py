"""1. Na sygnale z poprzednich zajęć zastosować filtr butterwortha:
a) Dolnoprzepustowy (pozostawić jedynie najmniejszą częstotliwość)
b) Górnoprzepustowy (pozostawić jedynie największą częstotliwość)
c) Pasmowo przepustowy (pozostawić jedynie środkową częstotliwość)
2. W jednym oknie przedstawić sygnał oryginalny i sygnały po zastosowaniu wszystkich filtrów
3. W jednym oknie przedstawić FFT wszystkich sygnałów
4. Przedstawić spectrogram sygnału oryginalnego"""

import scipy.signal as sig
import numpy as np
import matplotlib.pyplot as plt

def filtr():
    t = 10  # czas trwania
    fs = 1000  # częstotliwość próbkowania
    f = 5  # częstotliwość sygnału
    A = 3  # amplituda

    x = np.linspace(0, 1, fs, False)  # 1 sekunda
    y = A * np.sin(2 * np.pi * 50 * x)
    y += A * np.sin(2 * np.pi * 150 * x)
    y += A * np.sin(2 * np.pi * 300 * x)

    # Filtracja sygnału
    def butter_highpass(signal, cutoff, fs):
        sos = sig.butter(8, cutoff, 'high', fs=fs, output='sos')
        return sig.sosfilt(sos, signal)

    def butter_lowpass(signal, cutoff, fs):
        sos = sig.butter(8, cutoff, 'low', fs=fs, output='sos')
        return sig.sosfilt(sos, signal)

    def butter_bandpass(signal, lowcut, highcut, fs):
        sos = sig.butter(8, [lowcut, highcut], 'band', fs=fs, output='sos')
        return sig.sosfilt(sos, signal)

    filtered_signalH = butter_highpass(y, 200, fs)  # Górnoprzepustowy - usuwa poniżej 40 Hz
    filtered_signalL = butter_lowpass(y, 100, fs)  # Dolnoprzepustowy - usuwa powyżej 40 Hz
    filtered_signalB = butter_bandpass(y, 100, 200, fs)  # Pasmo 40-100 Hz

    # Rysowanie wyników
    plt.figure(figsize=(18, 9))

    plt.subplot(4, 1, 1)
    plt.plot(x, y, 'g')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.title('Oryginalny sygnał sinusoidalny')

    plt.subplot(4, 1, 2)
    plt.plot(x, filtered_signalH, 'r')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.title('Sygnał po filtracji górnoprzepustowej (Highpass)')

    plt.subplot(4, 1, 3)
    plt.plot(x, filtered_signalL, 'b')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.title('Sygnał po filtracji dolnoprzepustowej (Lowpass)')

    plt.subplot(4, 1, 4)
    plt.plot(x, filtered_signalB, 'm')
    plt.xlabel('Czas [s]')
    plt.ylabel('Amplituda')
    plt.title('Sygnał po filtracji pasmowoprzepustowej (Bandpass)')

    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Funkcja do obliczania FFT
    def compute_fft(signal, fs):
        N = len(signal)
        signal_fft = np.fft.rfft(signal)  # Obliczanie FFT (tylko dodatnie częstotliwości)
        freqs = np.fft.rfftfreq(N, 1/fs)  # Odpowiednie częstotliwości
        amplitudes_fft = np.abs(signal_fft)  # Amplituda FFT
        return freqs, amplitudes_fft

    # Obliczanie FFT dla każdego sygnału
    freq_orig, fft_orig = compute_fft(y, fs)
    freq_high, fft_high = compute_fft(filtered_signalH, fs)
    freq_low, fft_low = compute_fft(filtered_signalL, fs)
    freq_band, fft_band = compute_fft(filtered_signalB, fs)

    # Rysowanie wykresu
    plt.figure(figsize=(18, 9))
    plt.subplot(4, 1, 1)
    plt.plot(freq_orig, fft_orig)
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('FFT - Oryginalny sygnał"')

    plt.subplot(4, 1, 2)
    plt.plot(freq_high, fft_high)
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('FFT - Górnoprzepustowy (Highpass)')

    plt.subplot(4, 1, 3)
    plt.plot(freq_low, fft_low)
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('FFT - Dolnoprzepustowy (Lowpass)')

    plt.subplot(4, 1, 4)
    plt.plot(freq_band, fft_band)
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('FFT - Pasmowoprzepustowy (Bandpass)')

    plt.grid(True)  # siatka
    plt.tight_layout()  # dopasowanie wykresu
    plt.show()  # wyświetlenie wykresu
filtr()

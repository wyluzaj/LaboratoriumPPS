import numpy as np
import matplotlib.pyplot as plt
import time

# Funkcja DFT
def dft(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    return np.dot(e, signal)

# Generowanie sygnału
t = 10          # czas trwania w sekundach
fs = 100        # częstotliwość próbkowania w Hz
f = 5           # częstotliwość podstawowego sygnału w Hz
A = 3           # amplituda
x = np.linspace(0, t, fs * t)  # Oś czasu
y = A * np.sin(2 * np.pi * f * x)  # Sygnał podstawowy
y += 0.7 * np.sin(2 * np.pi * 10 * x)  # Dodatkowa składowa
y += 1.1 * np.sin(2 * np.pi * 15 * x)  # Dodatkowa składowa

# Obliczenie FFT
start_fft = time.perf_counter()
y_fft = np.fft.fft(y)
end_fft = time.perf_counter()
fft_time = end_fft - start_fft

# Obliczenie DFT
start_dft = time.perf_counter()
y_dft = dft(y)
end_dft = time.perf_counter()
dft_time = end_dft - start_dft

# Przygotowanie danych do wykresu
N = len(y)
freqs = np.fft.fftfreq(N, d=1/fs)
amplitudes_fft = np.abs(y_fft[:N//2])  # Amplituda FFT (pierwsza połowa)
amplitudes_dft = np.abs(y_dft[:N//2])  # Amplituda DFT (pierwsza połowa)
freqs_positive = freqs[:N//2]  # Dodatnie częstotliwości

# Wykresy
plt.figure(figsize=(18, 10))

# Wykres oryginalnego sygnału
plt.subplot(3, 1, 1)
plt.plot(x, y, label="Sygnał oryginalny")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")
plt.title("Sygnał w dziedzinie czasu")
plt.legend()

# Wykres FFT
plt.subplot(3, 1, 2)
plt.plot(freqs_positive, amplitudes_fft, label="FFT")
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo amplitudowe FFT")
plt.legend()

# Wykres DFT
plt.subplot(3, 1, 3)
plt.plot(freqs_positive, amplitudes_dft, label="DFT", color='orange')
plt.xlabel("Częstotliwość [Hz]")
plt.ylabel("Amplituda")
plt.title("Widmo amplitudowe DFT")
plt.legend()

plt.tight_layout()
plt.show()

# Wyświetlenie czasu obliczeń
print(f"Czas wykonania FFT: {fft_time:.5f} sekund")
print(f"Czas wykonania DFT: {dft_time:.5f} sekund")

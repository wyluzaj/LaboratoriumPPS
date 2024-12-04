"""1.Program implementujący DFT = Σ Xn e^((-2πjkn)/ N)
√(Re^2 + Im^2)
Xn - próbka nr n
e - np.exp
j - jednostka urojona
k = n.reshape((N, 1))
a.      Do sygnału z poprzednich zajęć dodać 2 składowe o różnych częstotliwościach i amplitudach
b.      Wyświetlić na jednym plocie oryginalny sygnał sinusoidalny i DFT
c.      Na wykresie DFT uwzględnić tylko pierwszą połowę sygnału
d.      Dodać funkcję FFT z biblioteki numpy i porównać czas wykonywania obu algorytmów"""

import time
import numpy as np
import matplotlib.pyplot as plt

def dft(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, x)
    return X

def sinus():
    t = 10 #czas trwania
    fs = 100 # czestotliwość próbkowania
    f = 5 #częstotliwość sygnału
    A = 3 #amplituda

    x = np.linspace(0, t, fs * t) # start - 0,  czas_trwania, czaestotliwość_próbkowania*czas_trwania

    # s(t)=Asin(2πf)
    #y = A * np.sin(x * 2 * np.pi * f) #Amplituda * sin(2 * pi * oś czasu * częstotliwość_sygnału)
    y = A * np.sin(x * f * 2 * np.pi)
    y += 0.7 * np.sin(x * 3 * 2 * np.pi)
    y += 1.1 * np.sin(x * 1 * 2 * np.pi)
    y += 0.3 * np.sin(x * 1 * 2 * np.pi)

    # Obliczanie czasu DFT
    t1 = time.perf_counter() # czas początkowy
    y_dft = dft(y) # wywołanie funkcji dft
    t2 = time.perf_counter() # czas końcowy
    dft_time = t2 - t1 # czas wykonania DFT

    # Obliczanie czasu FFT
    t1 = time.perf_counter() # czas początkowy
    y_fft = np.fft.fft(y) # wywołanie funkcji fft
    t2 = time.perf_counter() # czas końcowy
    fft_time = t2 - t1 # czas wykonania FFT

    plt.figure(figsize=(15, 7)) # okno wykresu

    #Oryginany sygnał sinusoidalny
    plt.subplot(2, 1, 1) # 2 wiersze, 1 kolumna, 1 wykres
    plt.plot(x, y, 'g') #wykres sygnału czasowego y w funkcji czasu x - zielony
    plt.xlabel('Czas')
    plt.ylabel('Amplituda')
    plt.title('Oryginalny sygnał sinusoidalny')

    #DFT
    plt.subplot(2, 1, 2) # 2 wiersze, 1 kolumna, 2 wykres
    plt.plot(np.abs(y_dft)[:len(y_dft)//2]) #wykres widma amplitudowego - połowa
    plt.xlabel('Częstotliwość')
    plt.ylabel('Amplituda')
    plt.title('Wykres funkcji DFT')

    plt.grid(True) # siatka
    plt.tight_layout() # dopasowanie wykresu
    plt.show() # wyświetlenie wykresu
    print(f"Czas wykonania DFT: {dft_time:.5f} sekund") # wyświetlenie czasu wykonania DFT z dokładnością do 5 miejsc po przecinku
    print(f"Czas wykonania FFT: {fft_time:.5f} sekund") # wyświetlenie czasu wykonania FFT z dokładnością do 5 miejsc po przecinku

sinus()
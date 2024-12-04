import numpy as np
import matplotlib.pyplot as plt

t = 10 #czas trwania
fs = 100 # czestotliwość próbkowania. Sto próbek na sekunde
f = 3 #częstotliwość sygnału. Sinus ma 3 pełnych okresów na sekundę
A = 2 #amplituda

n= fs*t #liczba próbek
x = np.linspace(0, t, n) # wektor czasu, który obejmuje 10 sekund, z n równomiernie rozmieszczonymi punktami.

#y=Asin(2πf)
y = A * np.sin(2 * np.pi * f * x) #f to częstotliwość sinusoidy, czyli ile pełnych cykli sygnału występuje w ciągu sekundy
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x), y')
plt.show()


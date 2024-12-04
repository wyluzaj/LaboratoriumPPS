import numpy as np
import matplotlib.pyplot as plt

t = 10 #czas trwania
fs = 100 # czestotliwość próbkowania
f = 5 #częstotliwość sygnału
A = 2 #amplituda

n= fs*t #liczba próbek
x = np.linspace(0, t, n) # start - 0,  czas_trwania, czaestotliwość_próbkowania*czas_trwania

#s(t)=Asin(2πf)
y = A * np.sin(x * 2 * np.pi * f)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x), y')
plt.show()


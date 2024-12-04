import numpy as np
import matplotlib.pyplot as plt

t = 10 #czas trwania
fs = 100 # czestotliwość próbkowania
f = 5 #częstotliwość sygnału
A = 2 #amplituda

x = np.linspace(0, t, fs*t)

y = (A * np.sin(x * 2 * np.pi * f)) #s(t)=Asin(2πf)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x), y')
plt.show()


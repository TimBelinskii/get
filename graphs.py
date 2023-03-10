import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

# Экспериментальные данные
data = pd.read_csv('data.csv')
X, Y = data['X'], data['Y']
x = np.linspace(X.min(), X.max(), 300)  # это для линий


# Аппроксимация функцией f
def f(x, a, b):
    return a * x + b
popt, pcov = curve_fit(f, X, Y)
a, b = popt

# Что-то вроде сплайна
g = interp1d(X, Y, kind='cubic')  # Это функция (Y = g(X))

# Графички
plt.plot(X, Y, 'o', x, f(x, a, b), '-', x, g(x), '-')
plt.show()
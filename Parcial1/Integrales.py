# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:17:05 2023
For: Parcial 1 Simulación 2023-2
@author: 21-407-JAC
"""
import numpy as np
import matplotlib.pyplot as plt
# Datos
x = np.linspace(0, 1, 1000)
# Parábola
y_parabola = 4 * x * (1-x)
# Elipse
y_ellipse_up = 0.25 * np.sqrt(1 - ((x-0.5)/0.5)**2) + 0.5
y_ellipse_down = -0.25 * np.sqrt(1 - ((x-0.5)/0.5)**2) + 0.5
# Seno
y_sine = 0.5 * np.sin(2 * np.pi * x) + 0.5
# Coseno
y_cosine = 0.5 * np.cos(2 * np.pi * x) + 0.5
# Función logística
y_logistic = 1 / (1 + np.exp(-12 * (x - 0.5)))
# Gráficas
plt.figure(figsize=(10, 10))

plt.plot(x, y_parabola, color='blue', label='Parabola')
plt.plot(x, y_ellipse_up, color='red', label='Elipse Superior')
plt.plot(x, y_ellipse_down, color='red', label='Elipse Inferior')
plt.plot(x, y_sine, color='green', label='Seno')
plt.plot(x, y_cosine, color='cyan', label='Coseno')
plt.plot(x, y_logistic, color='pink', label='Logística')
plt.legend()
plt.show()

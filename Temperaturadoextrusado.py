# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:06:03 2024

@author: Ana
"""

import numpy as np
import matplotlib.pyplot as plt

#Espaço
L = 0.7  
nx = 100  
delta_x = L / (nx - 1)  

#Tempo
dt= 0.1
nt = 100000

#Propriedades do polímero
k = 0.24  #condutividade térmica (W/m°C)
rho = 905  # densidade pp (kg/m³)
Cp = 1812.98  #calor específico (J/kg°C)
alpha = 1.45e-7  #difusividade térmica (m²/s)
q = 500  # Geração interna de calor (W/m³)


# Condições de contorno
T_entrada = 165  # temperatura na entrada (x = 0)
T_saida = 180  # temperatura na saída (x = L)

def dif_finita():
    y = np.ones(nx)*T_entrada
    y[-1] =T_saida
    
    for n in range(nt):
        y_new = y.copy()  
        for i in range(1, nx - 1):
            y_new[i] = y[i] + dt * (alpha * (y[i + 1] - 2 * y[i] + y[i - 1]) / (delta_x ** 2) + q / (rho * Cp))
       
        y = y_new
        
    return y
        
#Plot :)
x = np.linspace(0, L, nx)
y = dif_finita()
plt.rc('font', family='Times New Roman')
plt.plot(x, y, color="deeppink",linestyle=":")
plt.xlabel('Comprimento (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura ao longo do comprimento')
plt.legend()
plt.show()      
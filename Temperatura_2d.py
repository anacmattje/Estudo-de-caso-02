# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:45:58 2024

@author: Ana
"""
import numpy as np
import matplotlib.pyplot as plt

#Espaço em Z 
L = 0.7  
nz = 100  
delta_z = L / (nz - 1)  

# Espaço em R
r= 0.0175 
nr = 100
delta_r = r/(nr-1)

#Tempo
dt= 0.1
nt = 1000

#Propriedades do polímero
k = 0.24  #condutividade térmica (W/m°C)
rho = 905  # densidade pp (kg/m³)
Cp = 1812.98  #calor específico (J/kg°C)
alpha = 1.45e-7  #difusividade térmica (m²/s)
q = 500  # Geração interna de calor (W/m³)


# Condições de contorno em z 
T_entrada = 165  # temperatura na entrada (z = 0)
T_saida = 180  # temperatura na saída (z = L)

def dif_finita_2d():
    T = np.ones((nz,nr))*T_entrada #criar uma matriz T com dimensões nz e nr com T_entrada em todas as células.
    T[:,-1] =T_saida  #substituir a última coluna pot T_saida
    
    for n in range(nt):
        T_new = T.copy()  #cópia para não alterar o T original
        for i in range(1, nz - 1): #comprimento
         for j in range (1,nr-1): #raio
            r_j = j * delta_r
            termo_radial = (1 / r_j) * (T[i, j + 1] - T[i, j - 1]) / (2 * delta_r) + \
                         (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) / (delta_r ** 2)
            termo_axial = (T[i+1,j] - 2*T[i,j] + T[i-1,j])/delta_z**2
       
            T_new[i, j] = T[i, j] + dt * alpha * (termo_radial + termo_axial) + dt * (q / (rho * Cp))
        
        T = T_new
        
    return T
        
#Plot da temperatura radial
T = dif_finita_2d()
# posições_z = [int(nz / 2)]  # Temperatura em z = 0,35m
r = np.linspace(0, r, nr)

plt.rc('font', family='Times New Roman')
plt.plot(r, T[int(nz / 2), :], color="pink", label='z = 0.35 m')

plt.xlabel('Raio (m)')
plt.ylabel('Temperatura (°C)')
plt.title('Perfil de temperatura radial')
plt.legend()
plt.show()
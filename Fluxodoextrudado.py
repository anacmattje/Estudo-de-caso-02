# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:49:24 2024

@author: Ana
"""

import numpy as np
import matplotlib.pyplot as plt 
from math import pi 

#Calcular a velocidade(Ux) variando com a rotação do parafuso (rpm)
def rpm_para_mps(rpm):
    return (pi*0.035*rpm)/60

def m3ps_para_kgph(y):
    return y*950*3600  #950 é a densidade do HPDE (artigo)|3600 de s para h

#Cálculo do fluxo (Q)
def f (Ux,B,W,delta_p,viscosidade,Z):
    return (Ux*B*W)/2 - (W*(B**3)*delta_p)/(12*viscosidade*Z)

#Parâmetross para calcular o fluxo (Q)
Ux = 0.0916 # (m/s)
B = 0.0002 # (m)
w = 0.035 # (m)
delta_p = 1 #valor assumido (Pa)
viscosidade = 2 #(Pa.s)
Z = 0.7 # (m)

#Valores do eixo x (rpm parafuso) 
x = np.linspace (5,20,40)
#Valores do eixo y (Fluxo Q)
y = f(rpm_para_mps(x), B, w, delta_p, viscosidade, Z)

y = m3ps_para_kgph(y)

print(x)
print(y)

# Plotando o gráfico
plt.rc('font', family='Times New Roman')
plt.plot(x, y,color="deeppink",linestyle=":")
plt.xlabel("Rotação do parafuso (rpm)")
plt.ylabel("Q - Fluxo do Extrusado (kg/h)")
plt.title("Efeito da taxa de fluxo com a rotação")
plt.legend()
plt.show()
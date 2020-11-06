'''
O programa roda e fornece os resultados esperados.
Obs: A questão exigia a utilização de uma precisão relativa (|x_n-x_{n-1}|/x_n) de 1.e-7
'''

# -*- coding: utf-8 -*-
"""bissecao

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QDuEoIEzi7dgC4MwNdrgYJa1xh2ssrXm
"""

import matplotlib.pyplot as plt
import numpy as np

print("Esse programa implementa o método da bisseção para achar a primeira raiz positiva de f(x) = eˆ(-x) - sin(x*pi/2) ")

#função que desejamos encontrar a raiz
def f(x):
  return np.exp(-x) - np.sin(np.pi*x/2)

#faz o gráfico da função acima com os valores de x e y definidos
x = np.linspace(0,4,200)
y = f(x)
plt.plot(x,y)
plt.title("Função")
plt.grid(True)
plt.show()

xmax = float(input("Olhe o gráfico acima e determine o x máximo do intervalo desejado \n"))
xmin = float(input("Olhe o gráfico acima e determine o x mínimo do intervalo desejado \n"))
limite = 100  #número maximo de iterações
precisao = 1*10**-7
fmin = f(xmin)  #função com o valor de xmax
fmax= f(xmax)   #função com o valor de xmin

if fmin * fmax > 0:  
  print("Intervalo inadequado.")

else:
  Nit = 0  #contador para o número de iterações
  while abs(xmax - xmin) > precisao and Nit<limite:
    xmedio = (xmax + xmin)/2  #média dos valores
    fmedio = f(xmedio)        #função com o valor de xmedio
    if fmin * fmedio < 0:
      xmax = xmedio   
    else:
      xmin = xmedio
    Nit = Nit + 1

  print("O número de iterações : %.d \ne a raiz é %.3f" %(Nit,xmedio))
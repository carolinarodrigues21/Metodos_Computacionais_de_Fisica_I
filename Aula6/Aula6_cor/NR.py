'''
Gabriella
 - [linha 45] Erro na condição para o programa não rodar para um x
   inicial com derivada próxima de zero:
   usou '>' em vez de '<'
 - [linha 52] Erro na função para o valor da raíz:
   usou 'dxi' em vez de 'derivada(xi)'
   2.5/5
'''
# -*- coding: utf-8 -*-
"""NR

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QDuEoIEzi7dgC4MwNdrgYJa1xh2ssrXm
"""

import matplotlib.pyplot as plt
import numpy as np

print("Esse programa implementa o método Newton-Raphson de para achar a primeira raiz positiva de f(x) = eˆ(-x) - sin(x*pi/2) ")

#função que desejamos encontrar a raiz
def f(x):
  return np.exp(-x) - np.sin(np.pi*x/2)

#derivada da funcao f(x) calculada analiticamente
def derivada(x):
  return -np.exp(-x) - (1/2)*np.pi*np.cos(np.pi*x/2)

#faz o gráfico da função acima com os valores de x e y definidos
x = np.linspace(0,4,200)
y = f(x)
plt.plot(x,y)
plt.title("Função")
plt.grid(True)
plt.show()

xi = float(input("Olhe o gráfico acima e determine o x desejado \n"))
limite = 100  #número maximo de iterações
precisao = 1*10**-7
dxi = derivada(xi) #derivada no ponto xi
precisao_derivada = 1*10**-3

if abs(dxi) > precisao_derivada:  # numeros cujas derivadas não são zero, mas serão muito perto e darão uma raiz muito distante
  print("Não é possivel encontrar a raiz por este valor de x")

else:
  Nit = 0  #contador para o número de iterações
  delta = 100
  while abs(delta) > precisao and Nit<limite:
    x = xi - f(xi)/dxi        # valor próximo x que será usado
    delta = (x - xi)          #função com o valor de x
    xi = x
    Nit = Nit + 1
  print("O número de iterações : %.d \ne a raiz é %.3f" %(Nit,x))

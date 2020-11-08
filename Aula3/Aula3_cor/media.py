# -*- coding: utf-8 -*-
'''
- Sem erros.

OBS: Poderia ter feito uma breve introdução sobre do que se trata o programa (#linha 26)
OBS: Poucos comentários.
OBS: Perda de generalidade ao forçar as notas a serem inteiras. (linha 29)
OBS: Variável "quadrado" não foi utilizada.
OBS: Tomar cuidado com os prints. Não fica claro o que quer dizer com "a média com o codigo" ou "o desvio com o codigo"
OBS: Escolher melhor os nomes das variáveis a serem utilizadas. Os nomes "eqm" e "eqs" não são
grandes indicativos da real finalididade das variáveis.
'''

"""salvando

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QDuEoIEzi7dgC4MwNdrgYJa1xh2ssrXm
"""

# -*- coding: utf-8 -*-
import numpy as np
from math import *

print("esse programa quer calcular a média de uma turma de alunos, vendo quem reprovou e quem passou \n")  #correção

imp = np.loadtxt ("media.txt")   #importa o arquivo com a lista de notas dos alunos
notas = np.array(imp,float)      #transforma a lista em um array com numeros float

mi = sum(notas)/len(notas)      #media da turma calculada somando as notas e dividindo pelo número de alunos 
mean = np.mean(notas)           #media usando a funcao do python

somatorio = 0
for i in notas:
    somatorio += (i - mi)**2
desvio = sqrt(1/(len(notas) - 1) * somatorio) #calcula o desvio padrão das notas
std = np.std(notas)                           #desvio padrao usando a funcao do python

#verificar a aprovação dos alunos
aprovados = 0
reprovados = 0 
for x in notas:    
    if x >= 7:      
        aprovados +=1   #aumenta o numero de aprovados cada vez que entrar nesse loop
    elif x < 3:
       reprovados +=1   #aumenta o numero de reprovados cada vez que entrar nesse loop

print("essa turma tem %d alunos, a média de notas é %.1f e o desvio padrão é %.1f." %(len(notas), mi, desvio))
print("a média calculada com o artifício do python é %.1f" %(mean))
print("o desvio calculada com o artifício do python é %.1f \n" %(std))

print("o número de alunos aprovados foi: %d" %(aprovados))
print("o número de alunos reprovados foi: %d" %(reprovados))

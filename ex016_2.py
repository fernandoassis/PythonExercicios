#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#Importa a função Truncate da biblioteca Math para pegar apenas o número inteiro
from math import trunc
#Solicita que digite o número usando decimais
n = float(input('Digite um número real usando . para os decimais: '))
#Imprime na tela o valor digitado com apenas a porção inteira
print('O valor digitado foi {} e a sua porção inteira é {}' .format(n, trunc(n)))

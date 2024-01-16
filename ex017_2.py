#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#...Calcule e mostre o comprimento da hipotenusa.
#Importa a função hipotenusa da biblioteca matemática
from math import hypot
#Solicita o valor do cateto oposto e armazena na variável
co = float(input('Digite o valor do cateto oposto: '))
#Solicita o valor do cateto adjecente e armazena na variável
ca = float(input('Digite o valor do cateto adjacente: '))
#calcula a hipotenusa usando a função importada
hi = hypot(co, ca)
#Imprime na tela o valor da hipotenusa
print('O valor da hipotenusa é: {:.2f}' .format(hi))

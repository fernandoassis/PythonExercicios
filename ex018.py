#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#Importa as funções: radianos, sen, cosseno e tangente da biblioteca matemática
from math import radians, sin, cos, tan
#Solicita o ângulo desejado
angulo = float(input('Digite o valor do ângulo que você deseja: '))
#Faz os calculos de seno, cosseno e tangente
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
#Imprime os resultados na tela
print('O Ângulo solicitado foi {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.' .format(angulo, seno, cosseno, tangente))

#Crie um programa que responda o Antecessor e o Sucessor do número digitado.

#Solicita o número para ser analizado e armazena em variável.
n = int(input('Digite um número para saber o antecessor e o sucessor: '))

#Calcula o antecessor e o sucessor, armazenando em varáveis
a = n - 1
s = n + 1

#Imprime o resultado na tela
print('O antecessor de {} é {} e o sucessor é {}'.format(n, a, s))

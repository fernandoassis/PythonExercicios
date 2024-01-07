#Crie um programa que responda o Antecessor e o Sucessor do número digitado.

num = int(input('Digite um número para saber o antecessor e o sucessor: '))
a = num - 1
s = num + 1
print('O antecessor de {} é {} e o sucessor é {}'.format(num, a, s))

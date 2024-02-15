#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

frase = str(input('escreva seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: {}' .format(frase.upper()))
print('Seu nome em letrars minúsculas é: {}' .format(frase.lower()))
print('Seu nome tem ao todo {} letras.' .format(len(frase) - frase.count(' ')))
nome = frase.split()
print('Seu primeiro nome é: {} e tem {} letras' .format(nome[0], len(nome[0])))

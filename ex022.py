#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('escreva seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: {}' .format(nome.upper()))
print('Seu nome em letrars minúsculas é: {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras.' .format(len(nome) - nome.count(' ')))
separado = nome.split()
print('Seu primeiro nome é: {} e tem {} letras' .format(separado[0], len(separado[0])))

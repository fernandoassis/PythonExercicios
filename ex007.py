#Desenvolva um programa que receba duas notas do aluno e calcule a média.
#Mostra na tela o que será feito
print('Vamos analisar a média aritmética da nota do(a) aluno(a).')
#Recebe o nome e armazena em varíavel
a = str(input('Digite o noeme do(a) aluno(a): '))
#Recebe as notas e armazena em varável
n1 = float(input('Digite a Primeira nota do(a) aluno(a): '))
n2 = float(input("Digite a segunda nota do(a) aluno(a): "))
#Calcula e imprime a média aritmética na tela
print('A média aritmética do(a) aluno(a)(a) {} é: {}.' .format(a, ((n1+n2)/2)))

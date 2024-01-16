#O quer sortear a ordem de apresentação de trabalhos dos alunos.
#...Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#Importa a função shuffle da biblioteca random
from random import shuffle
#Solicita os nomes dos alunos e armazena nas respectivas varáveis
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
#Cria uma lsita com os nomes armazenados
lista = [a1, a2, a3, a4]
#Muda aleatóriamente a ordem dos nomes da lista
shuffle(lista)
#Imprime na tela os nomes da lsita de acordo com a nova ordem aleatória
print('A ordem de apresentação será: {}' .format(lista))

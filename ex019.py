#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#...Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#Importa a função choice da biblioteca random
from random import choice
#Solicita os nomes dos alunos e armazena nas respectivas varáveis
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quart aluno: '))
#Cria uma lsita com os nomes armazenados
lista =[a1, a2, a3, a4]
#Sorteia um dos nomes da lista
sorteado = choice(lista)
#Imprime na tela o nome sorteado.
print('O aluno sorteado foi: {}' .format(sorteado))

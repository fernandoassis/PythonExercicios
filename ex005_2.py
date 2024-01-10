#Crie um programa que responda o Antecessor e o Sucessor do número digitado.

#Solicita o número para ser analizado.
n = int(input('Digite um número para saber o antecessor e o sucessor: '))

#Imprime o resultado na tela. O cálculo de antecessor e sucessor éfeito no momento da impressão, sem armazenar e varável
print('O antecessor de {} é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

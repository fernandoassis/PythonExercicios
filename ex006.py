#Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.
#Solicita o número a ser analizado e calculado
n = int(input('Digite um número para calcularmos o dobro, o triplo e a raíz quadrada dele: '))
#Faz os cálculos e armazena em varáveis
d = n*2
t = n*3
r = n**(1/2)
#Imprime na tela os resultados.
print('O dobro de {} é {}.' .format(n, d))
print('O triplo de {} é {}.' .format(n, t))
print('A raíz quadrada de {} é {:.2f}.' .format(n, r))

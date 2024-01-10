#Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

n = int(input('Digite um número: '))

d = n*2
t = n*3
r = n**(1/2)

print('O dobro de {} é {}.' .format(n, d))
print('O triplo de {} é {}.' .format(n, t))
print('A raíz quadrada de {} é {}.' .format(n, r))

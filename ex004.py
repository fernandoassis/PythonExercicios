#Faça um programa que leia algo no teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a=input('Digite Algo: ')
#Lê e armazena o que foi digitado.

print('O tipo primitivo dessa valor é: ', type(a))
#Testa e mostra qual o tipo primitivo. Sempre será str por não ter sido declado o tipo primitivo antes do input.

print('Só tem espeços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanúmerico? ', a.isalnum())
print('Está em maiúsculo? ', a.isupper())
print('Está em minúsculo? ', a.islower)
print('Está captalizada? (Caps Lock acionado) ', a.istitle)
#No final da linha o a. é objeto com características e realiza funcionalidade através de atributo e método.
#... O teste foi feito através de método booleano, responsável por responder se é verdadeiro ou falso de acordo com o método escolhido.

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta ...
#...necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
#Solicita as dimensões da parede e armazena em variável
print('Digite as medidas solicitadas abaixo, para saber o quanto de tinta precisa comprar.')
larg = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))
#Calcula a área da parede
par = larg * alt
#Calcula a quantidade de tinta necessária
tinta = par / 2
#Imprime na tela a área da parede e a quantidade necessária de tinta
print('Sua parede tem {} m². Você precisará de {} litros de tinta para fazer a pintura da parede.' .format(par, tinta))

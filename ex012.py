#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#Solicita o preço a ser calculado com o desconto
p = float(input('Digite o preço do produto para saber o preço com desconto de 5%: R$'))
#Calcula o preço digitado descontando os 5%
np = p-(p/100)*5
#Imprime na tela o valor do produto com desconto e configurando para aparecer apenas 2 casas decimais.
print('O novo preço do produto com 5% de desconto é: R${:.2f}' .format(np))

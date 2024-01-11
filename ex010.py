#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Solicita o valor em Reais e armazena na varável
real =float(input('Digite o valor que você tem em Reais e quer saber a quantos Dólares equivale: R$'))
#Calcula o valor em dólar
dolar = real/4.89
#Imprime na tela o valor do Real equivalente em Dólar
print('Você tem R${:.2f}, o equivalente a US${:.2f}' .format(real, dolar))

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias...
#... pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Digite a quantidade de dias em que o carro ficou alugado: '))
kmp = float(input('Digite a quantidade de kms percorridos: '))
td = d*60
tkmp = kmp*0.15
talu = (d*60)+(kmp*0.15)
print('O valor total do aluguel foi: R${:.2f}. Pelos {} dias de uso + os {} kms rodados' .format(talu, d, kmp))

#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias...
#... pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#Solicita a quantidade de dias para calucar o valor referente aos dias
d = int(input('Digite a quantidade de dias em que o carro ficou alugado: '))
#Solicita a quantidade de kms para calucar o valor referente aos kms rodados
km = float(input('Digite a quantidade de kms percorridos: '))
#faz o cálculo dos valores de dias e kms rodados e soma os valores
talu = (d*60)+(km*0.15)
print('O valor total do aluguel foi: R${:.2f}. Pelos {} dias de uso + os {} kms rodados' .format(talu, d, km))

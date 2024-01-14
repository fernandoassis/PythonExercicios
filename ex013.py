#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#Solicita o valor do salário atual para calcular o acréscimo
s = float(input('Digite seu salário atual para saber como ficará com o aumento de 15%: R$'))
#Cálculo do acréscimo no salário
ns = s+(s/100)*15
#Imprime na tela o valor do salário com aumento.
print('Seu novo salário com o aumento de 15% é: R${:.2f}' .format(ns))

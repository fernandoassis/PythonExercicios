#Solicite que digite 2 números e some os números

num1=float(input('Digite o primeiro número da soma: '))
num2=float(input('Digite o segundo número da soma: '))
#solicita o número a ser digitado.
#Obs: É necessário declarar o tipo primitivo para que a soma seja realizada corretamente...
#... .Sem a declaração do tipo, a soma entenderá que são strings e apenas juntará os 2 números um ao lado do outro.

soma=num1+num2
#Faz a soma dos números digitados

print(f'A soma entre o número {num1} e o número {num2} é: {soma}')
#Escreve na tela o resultado da soma.
#Obs: f é usado para possibilitar que os números digitados sejam escritos no texto do resultado.

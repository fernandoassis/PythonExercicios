#Solicite que digite 2 números e some os números

num1=float(input('Digite o primeiro número da soma: '))
num2=float(input('Digite o segundo número da soma: '))
#solicita o número a ser digitado e armazenado na variável.
#Obs: É necessário declarar o tipo primitivo para que a soma seja realizada corretamente...
#... .Sem a declaração do tipo, a soma entenderá que são strings e apenas juntará os 2 números um ao lado do outro.

soma=num1+num2
#Faz a soma dos números digitados

print('A soma entre o número {} e o número {} é: {}' .format(num1, num2, soma))
#Escreve na tela o resultado da soma.
#Obs: .format é usado para possibilitar que os números digitados sejam identificados em ordem no texto do resultado.

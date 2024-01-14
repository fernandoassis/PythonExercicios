#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#Solicita a temperatura que será convertida de °C para °F
c = float(input('Digite a temperatura desejada em °C para saber o equivalente em °F: '))
#Cálcula a conversão de °C para °F
f = (c*1.8)+32
print('A temperatura de {:.1f}°C equivale à {:.1f}°F' .format(c, f))

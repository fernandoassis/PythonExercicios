#Escreva um programa que leia um valor em metros e o exiba em km, hm, dam, dm, cm, mm.
#Solicita o valor em metro.
dist = float(input('Digite uma diatância em metros:'))
#Calcula as medidas para conversão
km = dist/1000
hm = dist/100
dam = dist/10
dm = dist*10
cm = dist*100
mm =dist*1000
#Imprime na tela os valores das converções
print('A medida de {}m corresponde a {}km' .format(dist, km))
print('A medida de {}m corresponde a {}hm' .format(dist, hm))
print('A medida de {}m corresponde a {}dam' .format(dist, dam))
print('A medida de {}m corresponde a {}dm' .format(dist, dm))
print('A medida de {}m corresponde a {}cm' .format(dist, cm))
print('A medida de {}m corresponde a {}mm' .format(dist, mm))

### Tres amigos jogaram na loteria .###
### Caso eles ganhem , o premio deve ser repartido proporcionalmente ao valor que cada um deus para a realização da aposta####
## Faça um programa que leia quanto cada apostador investiu , o valor do premio , e imprima quanto cada um ganharia do premio ###
### com base no valor investido ####

valor1=float(input("digite o valor investido pelo apostador 1:"))
valor2=float(input("digite o valor investido pelos apostador 2 :"))
valor3=float(input("digite o valor investido pelos apostador 3 :"))
valorPremio=float(input("digite o valor do premio:"))

valorRece1=valorPremio/valor1-valorPremio
valorRece2=valorPremio/valor2-valorPremio
valorRece3=valorPremio/valor3-valorPremio

print("os valores respecitvos sao :" , valorRece1 , valorRece2 , valorRece3)

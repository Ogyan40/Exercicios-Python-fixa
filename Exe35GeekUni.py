### Sejam A e B os catetos de um triangulo , onde a hipotenusa é obtida pela equação:####
###hipotenusa= raiz quadrada de a**2+b++2 .###
### Faça um programa que receba valores de a e b e calcule o valor da hipotenusa atraves da equação. imprima o resultado dessa operaçao ###

a1=float(input("digite o valor de A :"))
b1=float(input("digite o valor de B:"))



import math

hip = math.sqrt(a1**2 + b1**2)

print(hip)
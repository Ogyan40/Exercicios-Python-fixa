### Escreva um programa que leia as coordenadas x e y de pontos R2 e calcule sua distancia da origem .###

import math

X=int(input("digite o valor de x:"))
y=int(input("digite o valor de y:"))

X1=(X-y)**2
result=math.sqrt(X1)

print("o valor da distancia é :", result)
### Uma empresa contrata um encanador a R$ 30,00 por dia #####
### faça um programa que solicite o numero de dias trabalhados pelo encanador e imprima a quantia liquida que devera ser paga .###
### Sabendo-se que são descontados 8% para imposto de renda####


Enca1=float(input("digite o numeros de dias trabalhados:"))

dias=Enca1*30
descdias=dias*0.08
resultfinal=dias-descdias

print("total a pagar liquido é:",resultfinal)

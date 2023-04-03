### Faça um programa que leia o valor da hora de trabalho (em reais) e numero de horas trabalhadas no mês.####
### Imprima o valor a ser pago ao funcionario , adicionado 10% sobre o valor calculado.###

horat=float(input(("digite o numero de horas trabalhadas:")))

valorHora=float(input(("Digite o valor das horas trabalhadas:")))

result=horat*valorHora
resultFinal=result*0.10

print("O Valor final do salario é ",result + resultFinal)
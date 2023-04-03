### Receba o salario base de um funcionario ###
### Calcule e imprima o salario a receber , sabendo-se que esse funcionario tem uma gratificação de 5%  sobre o salario base####
### Alem disso ele paga 7% de imposto sobree o salario base ####

salBase=float(input("digite o salario base:"))

salAcres=salBase *0.05 + salBase
DescSal=salAcres*0.07

salLiquido = salAcres - DescSal

print("O salario liquido é:", salLiquido)
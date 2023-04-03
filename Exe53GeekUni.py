### Faça um programa para ler as dimensões de um terreno (comprimento C  e largura L), bem como o preço do metro da tela P.####
### Imprima o custo para cercar este mesmo terreno com tela ###


L=float(input(("Digite o valor da largura:")))

C=float(input("digite o valor do comprimento:"))

valor=3.00

valorMetro= C*L
valorFinal=valorMetro*valor

print(("o valor final é:", valorFinal))
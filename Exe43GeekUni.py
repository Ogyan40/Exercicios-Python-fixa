### Escreva um programa de ajuda para vendedores.Apartir do valor total lido mostre #####
### O total a pagar com desconto de 10% #####
### o valor de cada parcela , no parcelamento de 3 vezes sem juros:###
### a comissão  de vendedor , no caso da venda ser a vista (5% sobre o valor com desconto)###
### a comissão do vendedor , no caso da venda ser parcelada(5% sobre o valor total)###


valorVenda= float(input("digite o valor da venda :"))
valorDesc=valorVenda * 0.1 - valorVenda
valorParcela=valorVenda/3
comiVendedor1=valorDesc*0.05
comiVendedor2 = valorVenda*0.05

print("O valor total pago com desconto será:", valorDesc)
print("O valor de cada parcela de 3X sera:" , valorParcela)
print("A comissão em caso de venda a vista sera :" , comiVendedor1)
print("A comissão em caso de parcelamento será:", comiVendedor2)
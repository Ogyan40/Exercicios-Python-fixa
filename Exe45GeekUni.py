### Faça um programa para converter uma letra maiuscula em uma minuscula .####
### Use a tabela ASCII para resolver o problema.####


maius = input("digite a letra:")


maius = ord(maius)+32
minus=chr(maius)


print(" A letra minuscula correspondente é :", minus)

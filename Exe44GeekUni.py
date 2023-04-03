### Receba a altura do degrau de uma escada e a altura que o usuario deseja alcançar subindo a escada.###
### Calcule e mostre quantos degraus o usuario devera subir para atingir seu objetivo ###

altuDegrau=(int(input("Digite a altura do degrau:")))
altuDesejada=(int(input("Digite a altura desejada:")))


numeroDegraus=altuDesejada/altuDegrau

print("O numero de degraus para atingir op objetivo é : " , numeroDegraus)
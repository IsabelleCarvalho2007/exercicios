peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = (peso/(altura*altura))
if imc <= 18.5:
    print("magreza")
elif imc <= 24.9:
    print("saudável")
elif imc <= 29.9:
    print("sobrepeso")
elif imc <= 34.9:
    print("obesidade grau 1")
elif imc <= 39.9:
    print("obesidade grau 2")
else:
    print("obesidade grau 3")                     

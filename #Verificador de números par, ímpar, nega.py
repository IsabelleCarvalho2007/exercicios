 #Verificador de números par, ímpar, negativo e positivo ou zero
numero=float(input("digite um número:"))
if numero > 0 and numero % 2 == 0:
    print("Número é positivo e par")
elif numero > 0 and numero % 3 == 0:
    print("Número é positivo e multíplo de três")
elif numero < 0 and numero % 2 != 0:
    print("Número é negativo e ímpar")
elif numero == 0:
    print("Número é Zero")
else:
    print("Esse número não está relacionado com os descritos acima")
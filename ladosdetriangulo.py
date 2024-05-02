
a = float(input("Digite o tamanho do primeiro lado: "))
b = float(input("Digite o tamanho do segundo lado: "))
c = float(input("Digite o tamanho do terceiro lado: "))
    
       #Tipos de triângulos
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')

       #Lados de um triângulo
a = int(input("Digite o tamanho do primeiro lado: "))
b = int(input("Digite o tamanho do segundo lado: "))
c = int(input("Digite o tamanho do terceiro lado: "))

       #Tipos de triângulos
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif a == 0 or b == 0 or c == 0:
    print("Não é um triangulo")
elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')   
else:
    print('Escaleno')
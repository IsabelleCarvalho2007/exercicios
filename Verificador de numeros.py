      #Verificador de número par,impar,positivo,negativo ou zero
numero = float(input('Digite um número: '))

        #Possíveis Casos
if numero  > 0  and numero % 2 == 0 :
    print("Número é Positivo e Par")
elif numero > 0 and numero % 3 == 0 :   
    print("Número é Positivo e Multiplo de três")
elif numero < 0 and numero % 2 != 0:
    print("Número é Impar e negativo")    
elif numero == 0:
    print("Número é Zero")
else:
    print("Este número não está relacionado com tais dados descritos a cima")         
    

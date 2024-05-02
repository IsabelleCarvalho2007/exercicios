print("bom dia ")
ano = int(input("Digite um ano para verificar:"))
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("é ano bissexto")
else:
    print("não é ano bissexto")
    

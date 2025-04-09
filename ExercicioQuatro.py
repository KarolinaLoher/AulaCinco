valor = int(input("Digite um valor: "))
if valor<=0:
    print("Valor inválido")
else:
    for pia in range(1,valor+1,1):
     print(pia, end=" ")


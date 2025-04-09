cont = 0
fora = 0
for x in range(0,10,1):
        num = int(input("Digite dez valores: "))
        if num>=10 and num<=20:
            cont = cont + 1
            #print(f"Está dentro do intervalo, {cont} ")
        else:
            fora = fora + 1
            #print(f"Está fora do intervalo {fora}")

print(f"A quantidade de números que está dentro do intervalo é {cont} ")
print(f"A quantidade de números que está fora do intervalo é {fora}")
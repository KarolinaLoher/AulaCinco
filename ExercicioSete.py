media = 0
nota = 0
soma = 0
for x in range(0,5,1):
    nota = float(input("Digite suas cinco notas: "))
    soma = soma + nota
media = soma / 5
print(media)
#ex 2

numeros = []
for n in range(10):
    numero = int(input(f"Digite o {n+1}º número inteiro: "))
    numeros.append(numero)

print("Números lidos:")

numeros.reverse()

for num in numeros:
    print(num)
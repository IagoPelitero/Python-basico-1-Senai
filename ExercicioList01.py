#Ex 1

numeros = []
for n in range(5):
    numero = int(input(f"Digite o {n+1}º número inteiro: "))
    numeros.append(numero)

print("Números lidos:")
for num in numeros:
    print(num)
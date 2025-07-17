#ex 4

soma = 0
media = 0

for x in range(5):
    numero = float(input(f"Digite o {x + 1}º número: "))
    soma += numero

media = soma / 5

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media:.2f}")
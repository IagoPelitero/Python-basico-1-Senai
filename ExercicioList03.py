#ex 3

notas = []

for i in range(4):
    while True:
            nota = float(input(f"Informe a nota {i + 1} (entre 0 e 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")

    notas.append(nota)

    media = sum(notas) / 4

print(f'{notas}')
print(f"A média das notas é {media}.")
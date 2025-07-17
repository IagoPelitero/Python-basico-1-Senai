#ex 7

vetor = []

for x in range(5):
  num = int(input(f'Digite o {x + 1}º número: '))
  vetor.append(num)

soma = sum(vetor)
mult = 1

for num in vetor:
  mult *= num

print(f'\nNúmeros digitados: {vetor}')
print(f'Soma dos números: {soma}')
print(f'Multiplicação dos números: {mult}')
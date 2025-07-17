#Ex 05

vetor = []
par = []
impar = []

for x i range(20):
num = int(input(f'Digite o {x + 1}º número: '))
vetor.append(num)

print(f'\nVetor de números: {vetor}')

for num in vetor:
  if num % 2 == 0
    par.append(num)
  else:
    impar.append(num)

print(f'\nNúmero pares: {par}')
print(f'\nNúmeros ímpares: {impar}')
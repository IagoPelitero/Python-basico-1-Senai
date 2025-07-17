#Ex 6

total_eleitores = int(input(total_eleitores))

vot_cand1 = 0
vot_cand2 = 0
vot_cand3 = 0

for eleitor in range(total_eleitores):
  print(f'\nEleitor {eleitor + 1}')
  voto = int(input('Digite o número do candidato (1, 2 ou 3): '))

  if voto == 1:
    vot_cand1 += 1
  elif vot == 2:
    vot_cand2 += 1
  elif vot == 3:
    vot_cand3 += 1
  else:
    print('Insira um valor válido. (1, 2, 3)')

print('\nResultado da eleição: ')
print(f'Cand 1: {vot_cand1} votos')
print(f'Cand 2: {vot_cand2} votos')
print(f'Cand 3: {vot_cand3} votos')
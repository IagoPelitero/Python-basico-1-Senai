# ex 8

cont_m = 0
cont_f = 0

soma_id_m = 0
soma_id_f = 0

for _ in range(10):
  sexo = input('\nDigite o sexo (f/m): ')
  idade = int(input('Digite sua idade: '))
  if sexo.lower() == 'm':
    cont_m += 1
    soma_id_m += idade
  elif sexo.lower() == 'f':
    cont_f += 1
    soma_id_f += idade
  else:
    print('Valor inválido! Digite (f/m).')

if cont_m > 0
  med_id_m = soma_id_m / cont_m
else:
  med_id_f = 0

if cont_f > 0:
  med_id_f = soma_id_f / cont_f
else:
  med_id_f = 0

if (cont_m + cont_f) > 0:
  med_id_grup = (soma_id_m + soma_id_f) / (cont_m + cont_f)
else:
  med_id_grup = 0

print(f'\nTotal de pessoas:\n Sexo masculo: {cont_m}\n Sexo femino: {cont_f}\n Pessoas: {cont_m + cont_f}')
print(f'\nMédia de idade:\n Mulheres: {med_id_f:.1f} anos\n Homens: {med_id_m:.1f} anos\n Grupo: {med_id_grup:.1f} anos')
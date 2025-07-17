print('Reservatório de água')
alt = float(input('Digite a altura(cm): '))
larg = float(input('Digite a largura(cm): '))
comp = float(input('Digite o comprimento(cm): '))
valor = float(input('Digite o consumo médio diário (litros/dia): '))

arm = alt * larg * comp

aut = arm / valor

if aut < 2:
  print(f'capacidade do reservatório é de: {arm}')
  print(f'autonomia de do reservatório é de: {aut}')
  print(f'consumo elevado')
elif aut > 2 and aut <= 7:
  print(f'capacidade do reservatório é de: {arm}')
  print(f'autonomia de do reservatório é de: {aut}')
  print(f'consumo moderado')
elif aut > 7:
  print(f'capacidade do reservatório é de: {arm}')
  print(f'autonomia de do reservatório é de: {aut}')
  print(f'consumo reduzido')
else:
  print('Valores não válidos')
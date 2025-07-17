notas = 0
qnt_notas = 0

while True:
  nota = float(input('Informe a nota(0 para sair)'))
  if nota == 0:
    break
  notas = notas + nota
  qnt_notas = qnt_notas +1
  if qnt_notas > 0:
    media = notas/ qnt_notas
    print(f"A quantidade de notas informada: {qnt_notas}")
    print(f'Média é de: {media:.2f}')
  else:
    print('Nenhuma nota informada')
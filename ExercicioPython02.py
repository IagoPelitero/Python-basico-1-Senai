#EX 2

notas = 0
qnt_notas = 0

while True:
    nota = float(input('Informe a nota: {0 oara sair}'))
    if nota == 0:
      break
    notas = notas + nota
    qnt_notas = qnt_notas +1
    if qnt_notas > 0:
      media = notas/qnt_notas
      print(f'Quantidade de notas informadas é de: {qnt_notas}')
      print(f'Média é de: {media:.1f}')
      else:
      print:('Nenhuma nota informada')
      
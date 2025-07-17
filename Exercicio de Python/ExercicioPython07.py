#EX tabuada

while True:
  acertos = 0
  erros = 0

  num = int(input('Digite o número para treinar a tabuada: '))
  mult = 1

  while mult <= 10:
    result = num * mult

    resp_usuario = int(input(f'{num} x {mult} = ?'))

    if resp_usuario == result:
      print('Correto!')
      acertos += 1
    else:
      print(f'Errado! o valor correto é {result}')
      erros += 1

      mult += 1

    prit(f'Total de acertos: {acertos}')
    print(f'Total de erros: {erros}')

    cont = input('Deseja treinar outra tabua? (sim/não): ')

    if cont.lower() != 'sim':
      break
#EX1

while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))
    if 0 < nota or nota >= 10:
      print('Valor inválido! Digite novamente.')
    else:
      print(f'Você digitou a nota: {nota}')
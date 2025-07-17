#Ex 9

while True:
  num = int(input('Digite um número: '))
  if num < 0:
    print('Insira um valor positivo.')
  else:
    result = 1
    for fat in range(1, num + 1):
      result *= fat
    print(f'\nO fatorial de {num} é {result}')
    break
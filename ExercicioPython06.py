#EX 6

soma = 0
numero = None

while numero != 0:
  numero = int(input('Digite um número {0 para sair}: '))
  soma += numero

  print(f'Soma dos números digitados {soma}')
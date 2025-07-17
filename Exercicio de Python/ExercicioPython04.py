#EX 4

numero = int(input('Digite um número inteiro positivo: '))
contador_digitos = 0

  while numero > 0:
    numero //= 10
    contador_digitos += 1

    print(f'O número possui {contados_digitos} digitos.')
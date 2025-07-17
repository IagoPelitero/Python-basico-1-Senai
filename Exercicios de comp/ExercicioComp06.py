num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
op = input('Qual operação?: ')

if op == 'soma' or op == 'SOMA' or op == 'Soma':
    soma = num1 + num2
    print(f'O resultado da soma é: {soma}')
elif op == 'sub' or op == 'subtração' or op == 'Subtração' or op == 'subtracao':
    sub = num1 - num2
    print(f'O resultado da subtração é: {sub}')
elif op == 'multiplicao' or op == 'multiplicação' or op == 'mult' or op == 'Multiplicação':
    mult = num1 * num2
elif op == 'div' or op == 'divisao' or op == 'Divisão' or op == 'divisão':
    div = num1 / num2
    print(f'A divisão dos números é: {div}')
else:
  print('Operação não incluída ou não existe no programa por enquanto!')
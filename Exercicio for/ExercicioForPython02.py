#Ex 2

for num in range(1):
    numero_inicial = int(input("Digite um número inicial: "))

    numero = numero_inicial
    multiplicador = 3

    while numero <= 999:
        print(f"O resultado do triplo do {numero_inicial}  é: {numero}")
        numero *= multiplicador
        multiplicador += 1

    print("Atingido o máximo 999 ou próximo.")
#ex 4

consoantes = "bcdfghjklmnpqrstvwxyz"
cons = []

for _ in range(10):
        char = input("Digite um caractere: ").lower()
        if char.isalpha() and char in consoantes:
            cons.append(char)

print(f"Consoantes encontradas: {cons}")
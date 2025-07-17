# ex 7

num = []

for numero in range(5, 100):
  if numero % 7 == 0 and numero % 5 != 0:
    num.append(numero)

print('Estes são números divíseis por 7, e não múltiplos de 5: ')
print(num)
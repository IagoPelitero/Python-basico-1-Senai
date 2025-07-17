nad = int(input('Digite sua idade: '))

if nad == 5 or nad <= 7 and nad > 5:
    print('Infantil A')
elif nad == 8 or nad <= 11 and nad > 5:
    print('Infantil B')
elif nad == 12 or nad == 13 and nad > 5:
    print('Juvenil A')
elif nad == 14 or nad <= 17 and nad > 5:
    print('Juvenil B')
elif nad >= 18:
    print('Adultos maiores de 18')
else:
    print('Idade não aceita')
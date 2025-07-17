estado_civil = input('Digite a letra inicial do seu estado cívil: ')

if estado_civil == 'C' or estado_civil == 'c':
    print('C - Casado')
elif estado_civil == 'S' or estado_civil == 's':
    print('S - Solteiro')
elif estado_civil == 'D' or estado_civil == 'd':
    print('D - Divorciado')
elif estado_civil == 'V' or estado_civil == 'v':
    print('V - Viúvo')
elif estado_civil == 'O' or estado_civil == 'o':
   print('O - Outros')
else:
    print('Letra não reconhecida!')
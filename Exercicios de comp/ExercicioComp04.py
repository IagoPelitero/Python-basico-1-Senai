voto = int(input('Digite sua idade: '))

if voto == 16 or voto < 18 or voto >= 70:
    print('O voto é facultativo (não obrigatório)')
else:
    print('O voto é obrigatório')
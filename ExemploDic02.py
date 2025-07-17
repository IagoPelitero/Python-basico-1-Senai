#gerar dicionários com listas (arrays, vetores)

carros = {
    'Lancer': [89000.98, 'Mitsubishi'],
    'Opala': [100000.00, 'GM'],
    '500': [35000.00, 'FIAT']
}

print('O valor do carro é de: ' + str(carros['Lancer'][0]) + ' reais.' + ' A marca do carro é: ' + str(carros['Lancer'][1]) + '.')

print(carros.items())
print(carros.values())
#Exemplos de dicionarios

carros = {
    'ka': 13000,
    'civic': 120000,
    'corola': 100000,
    'uno': 12000,
    'montana': 50000
}

#printar apenas um determinado valor
print(carros.values())

#Atruibuir um novo valor a uma variável chave:
carros['corola'] = 150000

print(carros['corola'])

#Deletar um intem

del carros['civic']

print(carros.items())
print(carros)

carros.pop('corola')

print(carros)
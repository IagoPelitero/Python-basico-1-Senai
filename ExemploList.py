nomes = [
    'Anderson',
    'Daniel',
    'Edson',
    'Airogla',
    'Leticia alaide',
    'Leticia carpes',
    'Iago',
    'Cleide',
    'Ariclenio',
    'Mônica',
    'Leonardo',
    'Iara',
    'Ruan',
    'Cassio',
    'Amanda',
    'Henrique',
    'Eric',
    'Hugo',
    'Jenifer'
]

# nomes.sort(reverse=True);

for nome in range(0, len(nomes)):
    # print(f'O {nome + 1}º é: {nomes[nome]}')

    nome_informado = str(input('Informe um nome: '))

    if nome_informado.capitalize() in nomes:
      print('Nome encontrado!')
    else:
      print('Nome não encontrado!')
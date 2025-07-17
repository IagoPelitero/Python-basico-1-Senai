#Ex 02

produtos = {
    'celular': 1500,
    'camera': 1000,
    'fone de ouvido': 800,
    'monitor': 2000
}


while True:
  produto = str(input('Informe o produto que queira pesquisar o preço: '))

  if produto in produtos:
    print(f'Produto {produto} custa {produtos[produto]}.')

  else:
    novo_produto = input('Produto não encontrado! Deseja cadastrar? (sim/não)')

    if novo_produto == 'sim':
      novo_produto = input('Informe o nome do produto: ').lower()
      valor = float(input('Informe o valor: '))

      produtos[novo_produto] = valor
      print(f'Produto {novo_produto} cadastrado com sucesso!')

      print('Nova tabela de preços')
      for produto, preco in produtos.items():
        print(f'-{produto}:{preco}')
      break

    else:
      print('Até logo!')
      break
#Ex 01

produtos = {
    'celular': 1500,
    'camera': 1000,
    'fone de ouvido': 800,
    'monitor': 2000
}


while True:
  produto = str(input('Informe o produto que queira pesquisar o preço: ')).lower()
  if produto in produtos:
    print(f'Produto {produto} custa {produtos[produto]}.')
    break
  else:
    print('Produto não encontrado! Tente novamente')
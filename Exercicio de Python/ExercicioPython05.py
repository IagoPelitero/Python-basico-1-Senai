#EX 5

while True:
  print('Confirmação de senha')

  senha = input('Digite sua senha: ')
  confirmacao_senha = input('Confirme sua senha: ')

  if senha != confirmacao_senha:
    print('Senha não confere com a inserida!')
  else:
    print('Senha ok!')
    break
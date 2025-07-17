#ex 10

for _ in range(2):
  nome_user = input('Digite o nome de usuário: ')
  senha = input('Digite a senha: ')

  if senha == nome_user:
    print('\nSenha e usuário não podem ser iguais!')
  else:
    print('\nRegistro feito com sucesso!')
    break
else:
  print('Tentativa excedidas tente mais tarde!')
#ex 5

while True:
  num_alunos = int(input('Digite o número de alunos na turma: '))
  if num_alunos <= 0:
    print('Digite um número inteiro positivo!')
  else:
    break

  idades = []
  somas_idade = 0

  for cont in range(num_alunos):
    while True:
      idade = int(input(f'\nDigite a idade do aluno {cont + 1}: '))
      if idade > 0:
        break
      else:
        print('Digite um número inteiro positivo!')

    idades.append(idade)
    soma_idade += idade

  media_idade = soma_idade / num_alunos

  if media_idade <= 25:
    clas = 'Jovem'
  elif media_idade <= 60:
    clas = 'Adulta'
  else:
    clas = 'Idosa'

  print(f'\n média da turma é {media_idade}, classificada como {clas}.')
#Ex 06

med_alunos = []

for x in range(6):
  print(f'\nDigite as notas do {x + 1}º aluno: ')
  n1 = float(input('Digite a primeira nota (entre 0 e 10): '))
  while n1 < 0 or n1 > 10:
    n1 = float(input('Nota inválida! Digite novamente (entre 0 e 10): '))

  n2 = float(input('Digite a segunda nota (entre 0 e 10): '))
  while n2 < 0 or n2 > 10:
    n2 = float(input('Nota inválida! Digite novamente (entre 0 e 10): '))
  n3 = float(input('Digite a terceira nota (entre 0 e 10): '))
  while n3 < 0 or n3 > 10:
    n3 = float(input('Nota inválida! Digite novamente (entre 0 e 10): '))

  n4 = float(input('Digite a quarta nota (entre 0 e 10): '))
  while n4 < 0 or n4 > 10:
    n4 = float(input('Nota inválida! Digite novamente (entre 0 e 10): '))


  media = (n1 + n2 + n3 + n4) / 4
  med_alunos.append(media)

alunos_aprovados = 0
for media in med_alunos:
  if media >= 7.0:
    alunos_aprovados += 1

print(f'\nNúmero de alunos com média maior ou igual a 7.0: {alunos_aprovados}')
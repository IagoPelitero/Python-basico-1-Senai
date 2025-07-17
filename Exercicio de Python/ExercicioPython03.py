#EX 3

while True:
  numero_turmas = int(input('Digite a quantidade de turmas: '))
  if numero_turmas <= 0:
    print('Número de turmas inválidos!')
    break

    turmas = 1
    total_alunos = 0

  while turmas <= numero_turmas:
    alunos_turma = int(input(f'Digite o número de alunos na turma {turmas}: '))
    if alunos_turma <= 0 or alunos_turma > 40:
      print('Númerod e alunos inválido!')
    else:
      total_alunos += alunos_turma

    turma += 1

    if numero_turma > 0:

    media_alunos = total_alunos/numero_turmas
    print(f'Média de aluno por turma é de: {media_alunos:.1f}')
    break
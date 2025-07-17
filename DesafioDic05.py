#Desafio

tarefas = []
print('Menu de opções!')

menu = ('\n1)Adionar uma tarefa a lista. \n2)Visualizar todas as tarefas na lista. \n3)Marcar uma tarefa como concluída. \n4)Remover uma tarefa da lista. \n5)Sair do programa')

print(menu)

digite = int(input('Digite uma opção acima: '))

while True:
  match digite:
    case 1:
      nova_tarefa = input('Adicione sua tarefa: ')
      tarefas.append(nova_tarefa)

    case 2:
      print(tarefas)
    case 3:
      print('Logo atualizaremos!')
    case 4:
      remover = input('Digite a tarefa que deseja remover: ')
      tarefas.remove(remover)
    case 5:
      print('Até logo!')
else:
  print('Opção inválida. Tente novamente.')
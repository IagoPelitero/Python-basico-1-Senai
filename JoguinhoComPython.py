#Joguinho

import random

class personagem:
  def __init__(self, nome):
    self.nome = nome
    self.vida = 100

  def atacar(self, outro):
    dano = random.randint(5, 15)
    outro.vida -= dano
    print(f'{self.nome} atacou {outro.nome} causando {dano} de dano.')
    return dano

  def defender(self):
    defesa = random.randint(5, 10)
    self.vida += defesa
    print(f'{self.nome} defendeu e recuperou {defesa} de vida')
    return defesa

  def ataque_especial(self, outro):
    dano_especial = random.randint(15, 30)
    outro.vida -= dano_especial
    print(f'O {self.nome} utilizou o ataque especial em {outro.nome} causando {dano_especial} de dano!')
    return dano_especial

  def esta_vivo(self):
    return self.vida > 0

  def mostrar_vida(self):
    print(f'{self.nome} tem {self.vida} de vida')

def escolher_personagem():
  nome = input('Informe o nome do seu personagem')
  return personagem(nome)

def escolher_opcoes():
  print('Escolha uma ação: ')
  print('[1] - Atacar')
  print('[2] - Defender')
  print('[3] - Ataque especial')

def obter_escolha():
  while True:
    escolha = input('Inorme o número de sua escolha: ')
    if escolha in ['1', '2', '3']:
      return int(escolha)
    else:
      print('Escolha inválida. Por favor, escolha 1, 2 ou 3!')

def main():
  print('Seja bem vido ao jogo de batalha Senai Stars')

  #Escolher os personagens
  print('Jogador 1, escolha seu personagem')
  jogador1 = escolher_personagem()
  print('Jogador 2, escolha seu personagem')
  jogador2 = escolher_personagem()

  jogador_atual = jogador1
  oponente = jogador2

  # Loop principal do jogo
  while jogador1.esta_vivo() and jogador2.esta_vivo():
    print()
    jogador_atual.mostrar_vida()
    oponente.mostrar_vida()
    print()

    escolher_opcoes()
    escolha = obter_escolha()

    if escolha == 1:
      jogador_atual.atacar(oponente)
    elif escolha == 2:
      jogador_atual.defender()
    elif escolha == 3:
      jogador_atual.ataque_especial(oponente)

    #Verificar se o oponente ainda está vido
    if not oponente.esta_vivo():
      print(f'{oponente.nome} foi derrotado {jogador_atual.nome} venceu! Fatalityyyyyyyy')
      break

    jogador_atual, oponente = oponente, jogador_atual

  print('Game Over')

if __name__ == '__main__':
  main()
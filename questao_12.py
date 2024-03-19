def diferença_de_pontos(pontos_jogador_1,pontos_jogador_2):
  if pontos_jogador_1 - pontos_jogador_2 >= 2:
    return ' \nJogador 1 é o Vencedor!\n '
  elif pontos_jogador_2 - pontos_jogador_1 >= 2:
    return ' \nJogador 2 é o Vencedor!\n '
  else:
    return 'CONTINUAR'

def main():
  print('Partida de Pingue-Pongue\n------------------------')
  print("""GANHA O PRIMEIRO A ATINGIR 21 PONTOS E A DIFERENÇA DE PONTOS FOR MAIOR OU IGUAL A 2
  >> CASO CONTRÁRIO, O PRIMEIRO A IMPOR UMA DIFERENÇA DE 2 PONTOS APÓS OS 21 PONTOS, VENCE!""")

  pontos_jogador_1 = 0
  pontos_jogador_2 = 0
  while pontos_jogador_1 < 21 and pontos_jogador_2 < 21:
    pontuador = int(input('Qual Jogador Pontuou na Rodada [ 1 ou 2 ] : '))
    
    if pontuador == 1:
      pontos_jogador_1 += 1
    elif pontuador == 2:
      pontos_jogador_2 += 1
    else:
      while pontuador != 1 and pontuador != 2:
        pontuador = int(input('NÚMERO INVÁLIDO, Qual Jogador Pontuou na Rodada [ 1 ou 2 ] : '))
        
        if pontuador == 1:
          pontos_jogador_1 += 1
        elif pontuador == 2:
          pontos_jogador_2 += 1
  resultado_final = diferença_de_pontos(pontos_jogador_1,pontos_jogador_2)

  while resultado_final == 'CONTINUAR':
    pontuador = int(input('Qual Jogador Pontuou na Rodada [ 1 ou 2 ] : '))
    
    if pontuador == 1:
      pontos_jogador_1 += 1
    elif pontuador == 2:
      pontos_jogador_2 += 1
    else:
      while pontuador != 1 and pontuador != 2:
        pontuador = int(input('NÚMERO INVÁLIDO, Qual Jogador Pontuou na Rodada [ 1 ou 2 ] : '))
        
        if pontuador == 1:
          pontos_jogador_1 += 1
        elif pontuador == 2:
          pontos_jogador_2 += 1
    resultado_final = diferença_de_pontos(pontos_jogador_1,pontos_jogador_2)
  print('_'*23)
  print(resultado_final)
  print('_'*23)

main()

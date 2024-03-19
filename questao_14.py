def porcentagem(opiniao,serra,dilma,ciro,indeciso,outros,nulo):
  total = opiniao + serra + dilma + ciro + indeciso + outros + nulo
  porcentagem_serra = (serra / total) * 100
  porcentagem_dilma = (dilma / total) * 100
  porcentagem_ciro = (ciro / total) * 100
  porcentagem_indeciso = (indeciso / total) * 100
  porcentagem_outros = (outros / total) * 100
  porcentagem_nulo = (nulo / total) * 100
  
  print(f"""======== RESULTADO DA PESQUISA ========
  TOTAL ENTREVISTADOS = {total}
  Serra = {porcentagem_serra:.1f}%
  Dilma = {porcentagem_dilma:.1f}%
  Ciro = {porcentagem_ciro:.1f}%
  Indeciso = {porcentagem_indeciso:.1f}%
  Outros = {porcentagem_outros:.1f}%
  Nulo = {porcentagem_nulo:.1f}%
  """)

def possibilidade_2_turno(serra,dilma,ciro,outros):
  votos_validos = serra + dilma + ciro + outros
  porcentagem_serra = (serra / votos_validos) * 100
  porcentagem_dilma = (dilma / votos_validos) * 100
  porcentagem_ciro = (ciro / votos_validos) * 100
  porcentagem_outros = (outros / votos_validos) * 100

  if porcentagem_serra > 50 or porcentagem_dilma > 50 or porcentagem_ciro > 50:
    print('Para esses Resultados, O 2º Turno é Possível')
  else:
    print('Para esses Resultados, O 2º Turno NÃO é Possível')

def main():
  print('Eleições Presidenciais\n-----------------------')
  print("""Serra [ 45 ]
Dilma [ 13 ]
Ciro Gomes [ 23 ]
Indeciso = [ 99 ], Outros [ 98 ], Nulo [ 0 ]
\033[32mSaída Do Programa\033[m [ -1 ]
-----------------------""")
  opiniao = ''
  serra = 0
  dilma = 0
  ciro = 0
  indeciso = 0
  outros = 0
  nulo = 0
  while opiniao != -1:
    opiniao = int(input('Digite o Número do seu Candidato : '))
    if opiniao != -1:
      print('REGISTRADO!')
      if opiniao == 45:
        serra += 1
      elif opiniao == 13:
        dilma += 1
      elif opiniao == 23:
        ciro += 1
      elif opiniao == 99:
        indeciso += 1
      elif opiniao == 98: 
        outros += 1
      elif opiniao == 0:
        nulo += 1
    else:
      print('--------------------\nPesquisa Encerrada')

  porcentagem_final = porcentagem(opiniao,serra,dilma,ciro,indeciso,outros,nulo)
  possibilidade_2_turnosegundo_turno = possibilidade_2_turno(serra,dilma,ciro,outros)
  
main()

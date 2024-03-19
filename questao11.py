def media(nota_1,nota_2,nota_3):
  media = ((2*nota_1) + (3*nota_2) + (5*nota_3)) / 10
  return media

def main():
  print('Boletim Geral\n----------------------')
  matricula = ''
  aprovados = 0
  reprovados = 0
  alunos_totais = 0
  while matricula != 0:
    matricula = int(input('Digite sua Matrícula : '))
    
    if matricula != 0:
      nota_1 = float(input('Digite sua 1º Nota : '))
      nota_2 = float(input('Digite sua 2º Nota : '))
      nota_3 = float(input('Digite sua 3º Nota : '))
      print('_'*23)
      media_final = media(nota_1,nota_2,nota_3)
      alunos_totais += 1
  
      if media_final >= 7:
        aprovados += 1
      else:
        reprovados += 1

  print(' \n===========RESULTADO GERAL=============')
  print(f"""NÚMERO DE ALUNOS :  [{alunos_totais}]
ALUNOS APROVADOS :  [{aprovados}]
ALUNOS REPROVADOS : [{reprovados}]""")

main()

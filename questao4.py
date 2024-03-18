def main():
  print('Divisões sucessivas por 2')
  print('>> Até a divisão ser menor que 1\n------------------')
  N = int(input('Número: '))
  
  Sequencia = 0
  Resultado = 1
  while Resultado >= 1:
      Resultado = N / 2
      N = Resultado
  print(f'_____________________\nÚltima divisão sucessiva por 2 realizada: {N}')

main()

def main():
  print('Divisões sucessivas por 2')
  print('>> Até a divisão ser menor que 1\n------------------')
  n = float(input('Número: '))

  sequencia = 0
  resultado = 1
  while resultado >= 1:
      resultado = n / 2
      n = resultado
  print(f'_____________________\nÚltima divisão sucessiva por 2 realizada: {n}')

main()

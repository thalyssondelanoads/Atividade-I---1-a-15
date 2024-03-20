def main():
  print('Divisão caótica')
  print('>> Até N ser igual a 2\n-------------------------')
  x = int(input('Digite o 1º valor: ')) 
  n = int(input('Digite o 2º valor: '))
  
  resultado = 1
  while n >= 2:
      resultado = x / n
      print(f' {x} / {n} = {resultado}')
      n -= 1
      x = resultado

main()

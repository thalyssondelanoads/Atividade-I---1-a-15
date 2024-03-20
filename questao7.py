def main():
  print('Número Igual ao 1º Número\n------------------------------')
  n1 = float(input('Digite um Número: '))
  print('__________________________')

  n = 0
  while n != n1:
      n = float(input('Digite outro Número: '))
  print(f'-------------------------------\n0 Número {n} foi o Primeiro a ser Digitado')

main()

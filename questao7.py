def main():
  print('Número igual ao 1º número\n------------------------------')
  n1 = float(input('Digite um número: '))
  print('__________________________')
  
  n = 0
  while n != n1:
      n = float(input('Digite outro número: '))
  print(f'-------------------------------\n0 número {n} foi o primeiro a ser digitado')

main()

def main():
  print('Divisores dos números')
  print('>> Digite 0 para sair\n------------------')
  
  n = '' 
  while n != 0: 
      n = int(input('Digite o número: '))
      sequencia = 1
      while sequencia <= n: 
          if n % sequencia == 0:
              print(f'{sequencia}')
          sequencia += 1
  print('======= FINALIZADO =======')

main()

def main():
  print('Divisores dos números')
  print('>> Digite 0 para sair\n------------------')
  
  n = '' 
  while n != 0: 
      n = int(input('Digite o número: '))
      Sequencia = 1
      while Sequencia <= n: 
          if n % Sequencia == 0:
              print(f'{Sequencia}')
          Sequencia += 1
  print('======= FINALIZADO =======')

main()

def main():
  print('Divisores dos números')
  print('>> Digite 0 para sair\n------------------')
  
  N = '' 
  while N != 0: 
      N = int(input('Digite o número: '))
      Sequencia = 1
      while Sequencia <= N: 
          if N % Sequencia == 0:
              print(f'{Sequencia}')
          Sequencia += 1
  print('======= FINALIZADO =======')

main()

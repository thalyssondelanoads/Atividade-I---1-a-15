def main():
  print('MMC de Dois Números\n--------------------')
  Valor_a = int(input('Digite o 1º valor: '))
  Valor_b = int(input('Digite o 2º valor: '))
  
  Mmc = 1
  while Mmc % Valor_a != 0 or Mmc % Valor_b != 0:
      Mmc += 1
  print(f'__________________\nO MMC de {Valor_a} e {Valor_b} é [ {Mmc} ]')

main()

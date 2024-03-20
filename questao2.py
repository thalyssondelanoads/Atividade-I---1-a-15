def main():
  print('MMC de Dois Números\n--------------------')
  valor_a = int(input('Digite o 1º valor: '))
  valor_b = int(input('Digite o 2º valor: '))

  mmc = 1
  while mmc % valor_a != 0 or mmc % valor_b != 0:
      mmc += 1
  print(f'__________________\nO MMC de {valor_a} e {valor_b} é [ {mmc} ]')

main()

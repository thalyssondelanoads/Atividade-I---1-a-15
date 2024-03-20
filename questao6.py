def main():
  print('Número de Dígitos de um Número\n-----------------------------')
  numero = abs(int(input('Digite o número: ')))

  digitos = 0
  while numero % 10 > 1:
    numero /= 10
    digitos += 1
  print(f'____________\nO Número tem {digitos} Dígito(s)')
     
main()

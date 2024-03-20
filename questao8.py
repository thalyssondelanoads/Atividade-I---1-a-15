def main():
  print('Soma de Dois Números Consecutivos Igual a X\n------------------')
  x = int(input('Digite o Número X: '))

  numero = 0
  numero2 = 0
  while numero + numero2 != x:
      numero = int(input('Digite um Número: '))
      numero2 = int(input('Digite outro Número: '))
      
      if numero + numero2 == x:
        print(f'__________________\nA Soma de {numero} + {numero2} é igual a {x}')

main()

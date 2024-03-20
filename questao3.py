def main():
  print('MDC de Dois Números\n---------------')
  numero1 = int(input('Digite o 1º Valor: '))
  numero2 = int(input('Digite o 2º Valor: '))
  
  a, b = numero1, numero2
  while b != 0:
      a, b = b, a % b
  resultado_mdc = a
  print(f'_________________\nO MDC de {numero1} e {numero2} é [{resultado_mdc}]')

main()

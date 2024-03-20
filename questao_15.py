def decimal_para_binario(numero):
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        numero //= 2
    return binario

def decimal_para_hexadecimal(numero):
    if numero == 0:
        return '0'
    hexa = ''
    digitos_hexa = '0123456789ABCDEF'
    while numero > 0:
        resto = numero % 16
        hexa = digitos_hexa[resto] + hexa
        numero //= 16
    return hexa

def main():
    print('Conversor de Decimal para Binário e Hexadecimal')
    numero_decimal = int(input('Digite um Número entre 0 e 255: '))
    if numero_decimal < 0 or numero_decimal > 255:
        print('Número Inválido')
        return
    numero_binario = decimal_para_binario(numero_decimal)
    numero_hexadecimal = decimal_para_hexadecimal(numero_decimal)

    print(f'O número {numero_decimal} em binário é: {numero_binario}')
    print(f'O número {numero_decimal} em hexadecimal é: {numero_hexadecimal}')

main()

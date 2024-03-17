print('Divisão caótica')
print('>> Até N ser igual a 2\n-------------------------')
x = int(input('Digite o 1º valor: ')) #Solicita os dados ao usuário
n = int(input('Digite o 2º valor: '))

resultado = 1
while n >= 2: #Enquanto n não for 2, a variavel x recebe o valor de resultado e é subtraído 1 da variável n
    resultado = x / n
    print(f' {x} / {n} = {resultado}')
    n -= 1
    x = resultado

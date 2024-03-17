print('Divisões sucessivas por 2')
print('>> Até a divisão ser menor que 1\n------------------')
n = int(input('Número: ')) #Solicita os dados ao usuário

sequencia = 0
resultado = 1
while resultado >= 1: #Divide o valor n por 2 sucessivamente
    resultado = n / 2
    n = resultado
print(f'_____________________\nÚltima divisão sucessiva por 2 realizada: {n}')

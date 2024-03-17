print('Divisores dos números')
print('>> Digite 0 para sair\n------------------')

n = '' 
while n != 0: #Verifica se a variável NÃO é o flag número(0)
    n = int(input('Digite o número: ')) #Solicita os dados ao usuário
    sequencia = 1
    while sequencia <= n: 
        if n % sequencia == 0: #Verifica se cada valor é divisível pelo número
            print(f'{sequencia}')
        sequencia += 1
print('======= FINALIZADO =======')

print('MMC de dois números\n--------------------')
valor_a = int(input('Digite o 1º valor: ')) #Solicita os dados ao usuário
valor_b = int(input('Digite o 2º valor: '))

mmc = 1
while mmc % valor_a != 0 or mmc % valor_b != 0: #Verifica se a variavel é o mmc de ambos os valores
    mmc += 1
print(f'__________________\nO MMC de {valor_a} e {valor_b} é [ {mmc} ]')

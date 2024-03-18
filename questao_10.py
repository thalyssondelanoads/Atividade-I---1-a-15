def main():
    print('-' * 33)
    print('Teste de Combustivel e decolagem'.upper())
    print('-' * 33)

    Litros = float(input('Quantidade de Litros de Combustível[L]: '))
    while Litros < 10000:
        print('Quantidade Inferior ao Necessário')
        Litros = float(input('Quantidade de Litros de Combustível[L]: '))

    Peso_Combustivel = Litros * 1.5

    Total_Containers = abs(int(input('Quantidade Containers: ')))
    Contador_Containers = 0
    Peso_Total_Containers = 0
    while Contador_Containers != Total_Containers:
        Contador_Containers += 1
        Peso_Total_Containers += float(input('Peso do Container[KG]: '))

    Numero_Bilhete = int(input('Número do Bilhete: '))
    Contador_Malas = 0
    Contador_Pessoas = 0
    Peso_Malas = float()

    while Numero_Bilhete != 0:

        Contador_Pessoas += 1
        Quantidade_Malas_Da_Pessoa = int(input('Quantidade de Malas: '))
        Peso_Malas += Quantidade_Malas_Da_Pessoa * 10
        Numero_Bilhete = int(input('Número do Bilhete: '))

    Peso_Total_Passageiros = Contador_Pessoas * 70
    Peso_Passageiros_Malas = Peso_Total_Passageiros + Peso_Malas

    Peso_Decolagem = Peso_Combustivel + Peso_Total_Containers + Peso_Passageiros_Malas
    Possibilidade_Combustivel_Adicional = (500000 - Peso_Decolagem) / 1.5

    if(Possibilidade_Combustivel_Adicional < 0):
        Possibilidade_Combustivel_Adicional = 0

    print(f"""
Quantidade de Passageiros   : [{Contador_Pessoas}] Pessoa(s)
Peso Total de Bagagens      : [{Peso_Malas:.2f}] Kg
Peso dos Passageiros        : [{Peso_Total_Passageiros:.2f}] Kg
Peso da Carga               : [{Peso_Total_Containers:.2f}] Kg
Combustivel Extra           : [{Possibilidade_Combustivel_Adicional:.2f}] L
    """)

    if Peso_Decolagem <= 500000:
        print('-------[DECOLAGEM AUTORIZADA!]-------')
    else:
        print('-------[DECOLAGEM NÃO AUTORIZADA!]-------')


main()

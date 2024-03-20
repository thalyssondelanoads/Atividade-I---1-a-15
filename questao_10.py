def main():
    print('-' * 33)
    print('TESTE DE COMBUSTÍVEL E DECOLAGEM')
    print('-' * 33)

    litros = float(input('Quantidade de Litros de Combustível[L]: '))
    while litros < 10000:
        print('Quantidade Inferior ao Necessário')
        litros = float(input('Quantidade de Litros de Combustível[L]: '))

    peso_combustivel = litros * 1.5

    total_containers = abs(int(input('Quantidade Containers: ')))
    contador_containers = 0
    peso_total_containers = 0
    while contador_containers != total_containers:
        contador_containers += 1
        peso_total_containers += float(input('Peso do Container[KG]: '))

    numero_bilhete = int(input('Número do Bilhete: '))
    contador_malas = 0
    contador_pessoas = 0
    peso_malas = float()

    while numero_bilhete != 0:

        contador_pessoas += 1
        quantidade_malas_da_pessoa = int(input('Quantidade de Malas: '))
        peso_malas += quantidade_malas_da_pessoa * 10
        numero_bilhete = int(input('Número do Bilhete: '))

    peso_total_passageiros = contador_pessoas * 70
    peso_passageiros_malas = peso_total_passageiros + peso_malas

    peso_decolagem = peso_combustivel + peso_total_containers + peso_passageiros_malas
    peso_extra = 500000 - peso_decolagem

    if(peso_extra < 0):
        peso_extra = 0

    print(f"""
Quantidade de Passageiros   : [{contador_pessoas}] Pessoa(s)
Peso Total de Bagagens      : [{peso_malas:.2f}] Kg
Peso dos Passageiros        : [{peso_total_passageiros:.2f}] Kg
Peso da Carga               : [{peso_total_containers:.2f}] Kg
Peso Livre                  : [{peso_extra:.2f}] Kg
    """)

    if peso_decolagem <= 500000:
        print('-------[DECOLAGEM AUTORIZADA!]-------')
    else:
        print('-------[DECOLAGEM NÃO AUTORIZADA!]-------')

main()

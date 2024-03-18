print('Competição de Natação\n--------------------')

numero_prova = ''
qtd_nadadores = ''
n_nadadores = 0
contador = 0
pontuaçao_a = 0
pontuaçao_b = 0
while numero_prova != 0 and qtd_nadadores != 0:
    numero_prova = int(input('DIGITE O Nº DA PROVA: '))
    qtd_nadadores = int(input('DIGITE A QUANTIDADE DE NADADORES: '))
    print('_______________________')
    while contador < qtd_nadadores:
        contador += 1
        n_nadadores += 1
        nome_nadadores = str(input(f'Nome do nadador {n_nadadores}: '))
        classificaçao = int(input('Classificação: '))
        tempo = float(input('Tempo: '))
        clube = str(input('Clube [ a ] ou [ b ]: ')).lower()
        print('_______________________')
        
        if clube == 'a':
            if classificaçao == 1:
                pontuaçao_a += 9
            elif classificaçao == 2:
                pontuaçao_a += 6
            elif classificaçao == 3:
                pontuaçao_a += 4
            elif classificaçao == 4:
                pontuaçao_a += 3
            else:
                pontuaçao_a += 0
        elif clube == 'b':
            if classificaçao == 1:
                pontuaçao_b += 9
            elif classificaçao == 2:
                pontuaçao_b += 6
            elif classificaçao == 3:
                pontuaçao_b += 4
            elif classificaçao == 4:
                pontuaçao_b += 3
            else:
                pontuaçao_b += 0
        else:
            while clube != 'a' and clube != 'b':
                clube = str(input('Clube [ a ] ou [ b ]: ')).lower()
print('=============&=============')
print('     Resultado Oficial       ')
print(f' >> Pontuação Clube A: {pontuaçao_a}')
print(f' >> Pontuação Clube B: {pontuaçao_b}')
if pontuaçao_a > pontuaçao_b:
    print('_____________________\n VENCEDOR -> CLUBE A')
elif pontuaçao_b > pontuaçao_a:
    print('_____________________\n VENCEDOR -> CLUBE B')
else:
    print('_____________________\n VENCEDOR -> EMPATE')

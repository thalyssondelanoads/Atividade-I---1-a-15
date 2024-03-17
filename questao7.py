print('Número igual ao 1º número\n------------------------------')
n1 = float(input('Digite um número: ')) #Solicita os dados ao usuário
print('__________________________')

n = 0
while n != n1: #Verifica se a variàvel n é igual ao primeiro número digitado (n1)
    n = float(input('Digite outro número: '))
print(f'-------------------------------\n0 número {n} foi o primeiro a ser digitado')

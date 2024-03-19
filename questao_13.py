def reajuste_salario(salario):
  if salario < 3000:
    reajuste = salario + (salario * 0.25)
    return reajuste
  elif salario < 6000:
    reajuste = salario + (salario * 0.2)
    return reajuste
  elif salario < 10000:
    reajuste = salario + (salario * 0.15)
    return reajuste
  else:
    reajuste = salario + (salario * 0.1)
    return reajuste

def main():
  print('Reajustes de Salário\n----------------------')
  salario = ''
  soma_salarios = 0
  soma_novos_salarios = 0
  while salario != 0:
    salario = abs(float(input('Digite o Salário : ')))
    soma_salarios += salario
    novo_salario = reajuste_salario(salario)
    soma_novos_salarios += novo_salario
    diferença_salarios_e_novos_salarios = soma_novos_salarios - soma_salarios
    
    if salario != 0:
      print('======= RELATÓRIO SALARIAL =======')
      print(f"""Seu Novo Salário : R$ {novo_salario:.2f}
Soma dos Salários Atuais : R$ {soma_salarios:.2f}
Soma dos Salários Reajustados : R$ {soma_novos_salarios:.2f}
Diferença Entre as 2 Somas : R$ {diferença_salarios_e_novos_salarios:.2f}
==================================""")
    elif salario == 0:
      print('Programa Finalizado!')

main()

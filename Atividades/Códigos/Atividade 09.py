# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 09

# Aluno: Jetro Kepler, 2º Informática.

# 1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa em python usando funções que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# ● salários até R$ 280,00 (incluindo) : aumento de 20%
# ● salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# ● salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# ● salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# ● o salário antes do reajuste;
# ● o percentual de aumento aplicado;
# ● o valor do aumento;
# ● o novo salário, após o aumento.

def calcular_reajuste_salario(salario):
    if salario <= 280:
        percentual_aumento = 20
    elif salario > 280 and salario <= 700:
        percentual_aumento = 15
    elif salario > 700 and salario <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5
    
    valor_aumento = salario * percentual_aumento / 100
    novo_salario = salario + valor_aumento
    
    return salario, percentual_aumento, valor_aumento, novo_salario


salario = float(input("Digite o salário do colaborador: "))

salario_anterior, percentual_aumento, valor_aumento, novo_salario = calcular_reajuste_salario(salario)

print("Salário antes do reajuste: R$ {:.2f}".format(salario_anterior))
print("Percentual de aumento aplicado: {}%".format(percentual_aumento))
print("Valor do aumento: R$ {:.2f}".format(valor_aumento))
print("Novo salário, após o aumento: R$ {:.2f}".format(novo_salario))
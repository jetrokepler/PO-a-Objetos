# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 13

# Aluno: Jetro Kepler, 2º Informática.

# 1 - Crie um programa em Python que pede um número inteiro ao usuário e calcule seu fatorial.

def fatorial():

    num = int(input("Informe um número inteiro para que seu fatorial seja calculado: "))

    result = 1

    for i in range(1, num + 1):

        result *= i

    return result

print(fatorial())
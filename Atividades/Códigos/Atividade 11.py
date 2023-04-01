# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 11

# Aluno: Jetro Kepler, 2º Informática.

# 1 - Escreva um programa em Python que vai somar todos os números de 1 até 1 milhão, menos os que são múltiplos de 3.

def soma():

    total = 0

    for num in range(1, 1000000):

        if num % 3 != 0:

            total += num

    return total

print(soma())
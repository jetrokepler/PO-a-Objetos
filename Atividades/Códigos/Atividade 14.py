# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 14

# Aluno: Jetro Kepler, 2º Informática.

# 1 - Crie uma função que pede dois números, faz a soma e exibe o resultado, através de uma função. O usuário pode executar a função quantas vezes desejar.

def soma():

    print("Esse programa soma dois números.")

    num1 = int(input("Informe o 1º número: "))
    num2 = int(input("Informe o 2º número: "))

    total = num1 + num2
    print(f"A soma de {num1} + {num2} é igual a {total}")

while True:

    soma()

    executar = input("Deseja continuar? (s/n) ")

    if executar.lower() != "s":

        break
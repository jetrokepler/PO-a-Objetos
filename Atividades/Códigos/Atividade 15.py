# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 15

# Aluno: Jetro Kepler, 2º Informática.

# 1 - Faça uma calculadora, usando funções. O script pergunta qual operação o usuário deseja rodar (soma, subtração, multiplicação ou divisão) e executa a operação.
# A calculadora deve ser executada quantas vezes o usuário desejar.

def soma(a, b):

    return a + b

def subtracao(a, b):

    return a - b

def multiplicacao(a, b):

    return a * b

def divisao(a, b):

    if b == 0:

        return "Não é possível dividir por 0."
    
    else:

        return a / b

while True:

    print("CALCULADORA \nEscolha uma operação: \n1. Soma \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5): ")

    if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4" and escolha != "5":
    
        print("Escolha inválida. Tente novamente.")

        break

    if escolha == '5':

        break

    num1 = float(input("Digite o 1° número: "))
    num2 = float(input("Digite o 2° número: "))

    if escolha == '1':
        
        print(num1, "+", num2, "=", f"{soma(num1, num2):.2f}")

    elif escolha == '2':

        print(num1, "-", num2, "=", f"{subtracao(num1, num2):.2f}")

    elif escolha == '3':

        print(num1, "*", num2, "=", f"{multiplicacao(num1, num2):.2f}")

    elif escolha == '4':

        if isinstance(divisao(num1, num2), str):

            print(num1, "/", num2, "=", divisao(num1, num2))

        else:

            print(num1, "/", num2, "=", f"{divisao(num1, num2):.2f}")
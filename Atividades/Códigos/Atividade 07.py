# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 07

# Aluno: Jetro Kepler, 2º Informática.

# 1 - Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

class Numeros:

    def __init__(self):

        self.num1 = int(input("Informe o 1º número: "))
        self.num2 = int(input("Informe o 2º número: "))
        self.num3 = int(input("Informe o 3º número: "))

    def nummaior(self):

        return max(self.num1, self.num2, self.num3)
    
    def nummenor(self):

        return min(self.num1, self.num2, self.num3)
    
numeros = Numeros()
    
print(f"O mairo número é: {numeros.nummaior()} e o menor é: {numeros.nummenor()}.")
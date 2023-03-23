# Curso Técnico em Informática
# Programação Orientada a Objetos
# Exercício 08

# Aluno: Jetro Kepler, 2º Informática.

# 1 - Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
# ● A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# ● A mensagem "Reprovado", se a média for menor do que sete;
# ● A mensagem "Aprovado com Distinção", se a média for igual a dez.

class Media:

    def __init__(self):

        self.nota1 = float(input("Informe a 1º nota do aluno: "))
        self.nota2 = float(input("Informe a 2º nota do aluno: "))

    def calculo(self):

        return (self.nota1 + self.nota2) / 2
    
media = Media()

if media.calculo() >= 10:

    print(f"A média do aluno é: {media.calculo():,.2f}, aprovado com distinção!")

elif media.calculo() >= 7:

    print(f"A média do aluno é: {media.calculo():,.2f}, aprovado!")

else:

    print(f"A média do aluno é: {media.calculo():,.2f}, reprovado!")
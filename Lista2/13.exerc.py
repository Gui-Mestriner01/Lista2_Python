'''13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-
Segunda, etc.), se digitar outro valor deve aparecer valor inválido'''

num = int(input("Digite um número de 1 a 7 para ver o dia da semana correspondente: "))

dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

if num in dias_da_semana:
    print(f"O dia correspondente é: {dias_da_semana[num]}")
else:
    print("Valor inválido!")

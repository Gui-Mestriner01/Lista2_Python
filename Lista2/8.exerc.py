'''8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve
comprar, sabendo que a decisão é sempre pelo mais barato.'''

prod1 = float(input("Digite o valor que está o produto 1: "))
prod2 = float(input("Digite o valor que está o produto 2: "))
prod3 = float(input("Digite o valor que está o produto 3: "))

menor = min(prod1, prod2,prod3)

print("Você deve comprar o produto com menor preço", menor)
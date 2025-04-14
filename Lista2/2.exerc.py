'''2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

num = float(input("Digite um número, pode ser positivo ou negativo:"))

if num < 0:
    print("O número é negativo")
elif num > 0:
    print("O número é positivo")
else:
    print("O número digitado é zero")
'''7. Faça um Programa que leia três números e mostre o maior e o menor deles.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print("O maior número é:",maior)
print("O menor número é:",menor)

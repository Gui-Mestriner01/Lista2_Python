'''18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma
data válida.'''

from datetime import datetime

data_str = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    data_valida = datetime.strptime(data_str, "%d/%m/%Y")
    print("Válida!")
except ValueError:
    print("Inválida!")

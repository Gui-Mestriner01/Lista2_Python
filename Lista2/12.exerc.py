'''. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do
Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que
deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
o Desconto do IR:
o Salário Bruto até 900 (inclusive) - isento
o Salário Bruto até 1500 (inclusive) - desconto de 5%
o Salário Bruto até 2500 (inclusive) - desconto de 10%
o Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de
hora é 220.
o Salário Bruto: (5 * 220) : R$ 1100,00
o (-) IR (5%) : R$ 55,00
o (-) INSS ( 10%) : R$ 110,00
o FGTS (11%) : R$ 121,00
o Total de descontos : R$ 165,00
 Salário Liquido : R$ 935,00
'''

valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir_percentual = 0
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

inss_percentual = 10
sindicato_percentual = 3
fgts_percentual = 11

ir_valor = salario_bruto * (ir_percentual / 100)
inss_valor = salario_bruto * (inss_percentual / 100)
sindicato_valor = salario_bruto * (sindicato_percentual / 100)
fgts_valor = salario_bruto * (fgts_percentual / 100)

total_descontos = ir_valor + inss_valor + sindicato_valor
salario_liquido = salario_bruto - total_descontos

print("\n===== Folha de Pagamento =====")
print(f"Salário Bruto: ({valor_hora:.2f} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({ir_percentual}%) : R$ {ir_valor:.2f}")
print(f"(-) INSS ({inss_percentual}%) : R$ {inss_valor:.2f}")
print(f"(-) Sindicato ({sindicato_percentual}%) : R$ {sindicato_valor:.2f}")
print(f"FGTS ({fgts_percentual}%) : R$ {fgts_valor:.2f} (Depositado pela empresa)")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Líquido : R$ {salario_liquido:.2f}")

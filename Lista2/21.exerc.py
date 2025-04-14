'''21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do
saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão
as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa
não deve se preocupar com a quantidade de notas existentes na máquina.
o Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
o Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

def sacar_dinheiro(valor):
    if valor < 10 or valor > 600:
        return "O valor precisa ser entre 10 e 600 reais."

    notas = [100, 50, 10, 5, 1]
    resultado = []

    for nota in notas:
        quantidade = valor // nota
        if quantidade > 0:
            resultado.append(f"{quantidade} nota{'s' if quantidade > 1 else ''} de {nota} reais")
        valor %= nota

    return "\n".join(resultado)

valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))
print(sacar_dinheiro(valor_saque))

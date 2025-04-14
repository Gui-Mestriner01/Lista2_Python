'''19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de
centenas, dezenas e unidades do mesmo.
o Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111,
25, 20, 10, 21, 11, 1, 7 e 16'''

def decompor_numero(numero):
    if not (0 <= numero < 1000):
        return "Número inválido! Digite um número entre 0 e 999."

    centenas, resto = divmod(numero, 100)
    dezenas, unidades = divmod(resto, 10)

    partes = [
        f"{centenas} centena{'s' if centenas > 1 else ''}" if centenas else "",
        f"{dezenas} dezena{'s' if dezenas > 1 else ''}" if dezenas else "",
        f"{unidades} unidade{'s' if unidades > 1 else ''}" if unidades else "",
    ]

    return f"{numero} = " + " e ".join(filter(bool, partes))

'''Números que foram fornecidos'''
testes = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]

for numero in testes:
    print(decompor_numero(numero))

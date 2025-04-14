'''3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F
- Feminino, M - Masculino, Sexo Inválido.'''

sexo = input("Digite seu sexo: F(feminino) ou M(masculino)")

if sexo.upper() == 'M':
    print("Sexo Masculino")
elif sexo.upper() == 'F':
    print("Sexo Feminino")
else:
    print("Sexo inválido!")
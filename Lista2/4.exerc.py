'''4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input("Digite uma letra: ").strip().lower()


if len(letra) == 1 and letra.isalpha():
    if letra in "aeiou":
        print("A letra é uma vogal.")
    else:
        print("A letra é uma consoante.")
else:
    print("Por favor, digite apenas uma letra.")

#Outro jeito de fazer o exercicio.

if ('aeiou'.find(letra.upper()) >=0):
    print("Vogal")
else:
    print("Consonantal")
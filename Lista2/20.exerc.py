'''20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a
média alcançada por aluno e presentar:
o A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média
alcançada;
o A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média
alcançada;
o A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

n1 = float(input("Digite a 1ª nota: "))  
n2 = float(input("Digite a 2ª nota: "))  
n3 = float(input("Digite a 3ª nota: "))  

media = (n1 + n2 + n3) / 3  

if media == 10:  
    status = "Aprovado com Distinção"  
elif media >= 7:  
    status = "Aprovado"  
else:  
    status = "Reprovado"  

print(f"Média: {media:.1f} - {status}")  

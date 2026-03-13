"""
Desafio 090: Boletim Acadêmico com Dicionários.
Implementação de regras de negócio (Situação) integradas à estrutura 
de dados e exibição dinâmica via dicionário.items().
"""
ficha_aluno = {}

ficha_aluno['nome'] = str(input("Qual o nome do Aluno? ")).strip()
ficha_aluno['media'] = float(input("Qual a média do aluno? "))
while ficha_aluno['media'] < 0 or ficha_aluno['media'] > 10:
    print("A média do aluno precisa estar entre 0 e 10.")
    ficha_aluno['media'] = float(input("Qual a média do aluno? "))

if ficha_aluno['media'] <= 5:
    ficha_aluno['situação'] = 'REPROVADO'
elif ficha_aluno["media"] <= 7:
    ficha_aluno['situação'] = 'RECUPERAÇÃO'
else:
    ficha_aluno['situação'] = 'APROVADO'

print("-=" * 15)    
for k, v in ficha_aluno.items():
    print(f" - {k} é igual a {v}")
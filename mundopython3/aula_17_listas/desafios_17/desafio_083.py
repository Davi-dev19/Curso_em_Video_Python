"""
Desafio 083: Validação de expressões matemáticas através do gerenciamento de pilhas em Listas.
"""
pilha = []
expressao = str(input("Digite sua expressão: "))

for caracter in expressao:
    if caracter == "(":
        pilha.append("(")
    elif caracter == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
    
if len(pilha) == 0:
    print("Sua expressão é valida!")
else:
    print("Sua expressão é invalida!")
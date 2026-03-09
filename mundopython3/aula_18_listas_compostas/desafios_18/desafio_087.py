"""
Desafio 087: Análise de dados em matriz 3x3 (Soma de pares, colunas e valores máximos).
"""
matriz = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]
somatorio_pares = 0
somatorio_terceira_coluna = 0

for indice in range(0, 3):
    for posicao in range(0, 3):
        matriz[indice][posicao] = int(input("Digite um número: "))
    
for indice in range(0, 3):
    for posicao in range(0, 3):
        print(f"{matriz[indice][posicao]:^5}", end="")
    print()

for indice in range(0, 3):
    for posicao in range(0, 3):
        if matriz[indice][posicao] % 2 == 0:
            somatorio_pares += matriz[indice][posicao] 

        if posicao == 2:
            somatorio_terceira_coluna += matriz[indice][posicao] 
     
        if indice == 1:
            if posicao == 0:
                maior_valor_segunda_linha = matriz[indice][posicao] 
            else:
                if matriz[indice][posicao] > maior_valor_segunda_linha:
                    maior_valor_segunda_linha = matriz[indice][posicao] 

print(f"A soma de todos os valores pares digitado é: {somatorio_pares}.")
print(f"A soma dos valores da terceira coluna é: {somatorio_terceira_coluna}.")
print(f"O maior valor da segunda linha é: {maior_valor_segunda_linha}")
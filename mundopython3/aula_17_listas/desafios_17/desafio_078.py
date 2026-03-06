"""
Desafio 078: Manipulação de Listas dinâmicas e mapeamento de múltiplos índices de valores extremos.
"""
numeros = []

for indice in range(0, 5):
    numeros.append(int(input("Digite um número: ")))
print("-=-" * 30)

print(f"Os número digitados que foram para lista:")
for indice, numero in enumerate(numeros):
    print(f"{numero}", end=', ' if indice < 4 else ' ')
print("\n", "-=-" * 30)

maior_valor = max(numeros)
menor_valor = min(numeros)

print(f"O maior valor da lista: {maior_valor}. Que se encontra nos indices: ", end="")
for indice, valor in enumerate(numeros):
    if maior_valor == valor:
        print(f"{indice + 1}", end=" ")
print("\n", "-=-" * 30)

print(f"O menor valor da lista: {menor_valor}. Que se encontra nos indices: ",  end="")
for indice, valor in enumerate(numeros):
    if menor_valor == valor:
        print(f"{indice + 1}", end=" ")
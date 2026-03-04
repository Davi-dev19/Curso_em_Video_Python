a = [2, 9, 5, 6, 8]
b = a[:] # O valor de a foi copiado para b
b[2] = 7
print(f"A lista A contem: {a}")
print(f"A lista B contem: {b}")
# A solução para o problema do exemplo anterior é ao invés de fazer com que as duas memorias apontem para o mesmo valor.
# É Copiar somente o valor de uma variavel para a outra e só depois fazer a altteração. Dessa forma teremos duas listas diferentes.
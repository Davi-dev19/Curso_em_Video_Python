def dobra(list):
    pos = 0
    while pos < len(valores):
        valores[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# Dobramos os valores usando endereçamento de memoria.
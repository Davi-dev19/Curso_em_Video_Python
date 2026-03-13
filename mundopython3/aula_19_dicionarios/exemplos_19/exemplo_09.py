estado = dict()
brasil = []

for contador in range(1,4):
    estado["uf"] = str(input(f"Digite o {contador}° Estado Federativo: ")).strip()
    estado["sigla"] = str(input(f"Digite a Sigla do {contador}° Estado: ")).strip().upper()
    brasil.append(estado.copy())

print("-=" * 15)
for e in brasil:
    for v in e.values():
        print(v, end= ' ')
    print()
numeros = []

for contador in range(0,5):
    numeros.append(int(input("Digite um valor: ")))

for i, v in enumerate(numeros):
    print(f"Encontrei o valor {v} no indice {i}!")
print("Cheguei ao final da lista.")
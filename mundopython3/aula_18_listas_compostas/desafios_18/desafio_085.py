"""
Desafio 085: Listas com pares e ímpares (Matriz Fixa).
"""
numeros = [ [], []]

for numero in range(1,8):
    numero_usuario = int(input(f"Digite o número {numero}: "))
    if numero_usuario % 2 == 0:
        numeros[0].append(numero_usuario)
    else:
        numeros[1].append(numero_usuario)

numeros[0].sort()
numeros[1].sort()

print("-=-" * 15)
print(f"Os números impares digitados em ordem crescente foram: {numeros[1]}")
print(f"Os números pares digitados em ordem crescente foram {numeros[0]}")
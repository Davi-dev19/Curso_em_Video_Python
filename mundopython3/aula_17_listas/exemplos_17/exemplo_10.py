a = [2, 9, 5, 6, 8]
b = a # A partir do momento que fazemos isso as variaveis começam a apontar para o mesmo indereço de memória. Estão ligadas.
b[2] = 7 # Portanto qualquer alteração que fizer em uma também ocorrerá na outra.
print(f"A lista A contem: {a}")
print(f"A lista B contem: {b}")
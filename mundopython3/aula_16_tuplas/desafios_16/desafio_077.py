"""
Desafio 077: Identificação e extração de vogais em coleções de strings com Tuplas.
"""

ANIMAIS = ("cachorro", "gato", "elefante", "girafa", "hipopotamo", 
           "leao", "tartaruga", "zebra", "macaco", "tubarao", 
           "morcego", "avestruz")

for animal in ANIMAIS:
    print(f"\nNa palavra: {animal.upper()} temos as vogais: ", end="")
    for letras in animal:
        if letras.lower() in "aeiou":
            print(letras, end=" ")
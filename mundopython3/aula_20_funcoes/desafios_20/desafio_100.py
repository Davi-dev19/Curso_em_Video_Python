"""
Desafio 100: Sistema Modular de Sorteio e Análise de Pares.
Interação entre Funções: Passagem de Objetos por Referência (Listas Mutáveis).
Implementação de Pipeline de Dados: Geração Aleatória e Processamento Filtrado.
"""

from random import randint
from time import sleep
numeros = []


def sortear_numeros(numeros):
    '''Sorteando 5 valores aleatorios de 1 a 30'''
    print("Sorteando valores da lista:", end=' ', flush=True)

    for i in range(0, 5):
        numero_sorteado = randint(1, 30)
        numeros.append(numero_sorteado)
        print(f"{numero_sorteado}", end=' ', flush=True)
        sleep(0.5)
    print()


def somar_pares(lista):
    '''Buscando os números pares e a soma deles.'''
    total_pares = 0
    print("Somando os valores Pares de", end=' ')

    for numero in lista:
        if numero % 2 == 0:
            total_pares += numero
            print(f"{numero}", end=' ', flush=True)
            sleep(0.5)

    print(f"Temos {total_pares}")


sortear_numeros(numeros)
somar_pares(numeros)
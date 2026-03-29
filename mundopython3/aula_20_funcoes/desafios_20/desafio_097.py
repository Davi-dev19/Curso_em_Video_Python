"""
Desafio 097: Adaptador de Interfaces Textuais (Bordas Dinâmicas).
Manipulação de Strings: Formatação Adaptável ao Tamanho do Conteúdo.
Implementação de Funções de Utilidade para Padronização de UX no Terminal.
"""


def exibir_texto(txt):
    '''Exibindo bordas dinamicas.'''
    tamanho_texto = len(txt) + 4
    print("~" * tamanho_texto)
    print(f"{txt:^{tamanho_texto}}")
    print("~" * tamanho_texto)


texto = str(input("Digite um texto? ")).strip()
exibir_texto(texto)
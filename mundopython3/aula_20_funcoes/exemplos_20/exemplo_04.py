def somar(a, b):
    soma = a + b
    print(f"A = {a} e B = {b}.")
    print(f"A soma de A + B = {soma}")


somar(4, 5)
'''Podemos passar os argumentos para os parametros sem definir quem é quem, dessa forma os parametros receberão os 
argumentos na ordem em que os definimos.'''
somar(a = 4, b = 5)
somar(b = 4, a = 5)
'''Também é possivel definir em qual parametro o argumento será alocado.'''

def contador(*num):
    """
    Exemplo de empacotamento: conta e exibe os números recebidos.
    """
    tam = len(num)
    print(f'Recebi os valores {num} e ao todo são {tam} números.')


# Programa Principal (2 linhas abaixo da def)
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 8)
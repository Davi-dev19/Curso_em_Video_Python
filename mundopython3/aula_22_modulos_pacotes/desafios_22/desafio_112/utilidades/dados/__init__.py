def leia_dinheiro(msg):
    """
    --> Valida se a entrada é realmente um número decimal.
    :param msg: recebe preco.
    :return nenhum."""
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        
        if entrada.replace('.', '', 1).isdigit():
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido!\033[m')
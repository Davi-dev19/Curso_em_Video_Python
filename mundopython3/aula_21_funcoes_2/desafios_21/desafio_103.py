def analisar_ficha(jogador='<desconhecido>', gols = 0):
    """
    --> Exibe os dados tratados.
    :param jogador: Recebe o nome do Jogador.
    :param gols: Recebe a quantidade de gols do Jogador.
    :return: Nenhum Retorno """
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")


print("--" * 16)
nome_jogador = str(input("Nome do jogador: ")).strip()
gols_digitados = str(input("Números de gols: ")).strip()
if gols_digitados.isnumeric():
    quantidade_gols = int(gols_digitados)
else:
    quantidade_gols = 0

if nome_jogador == '':
    analisar_ficha(gols=quantidade_gols)
else:
    analisar_ficha(nome_jogador,quantidade_gols)
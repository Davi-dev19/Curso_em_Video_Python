Exception = exceção é um erro que não ocorre de forma frequente, ele não é um erro sintatico. Temos vários tipos de erros como esse, um exemplo comum é o erro de tipo: definimos que uma entrada deve ser um tipo, mas o usuário manda outro tipo de dado, resultando em TypeError no terminal. Para lidar com esses tipos de situação devemos tratar os dados, no Python temos dois comandos para fazer isso sendo eles: O try significa tente alguma coisa e o except se não acontece uma exceção. Também podemos usar um else apos o except e um finally para finalizar tudo. O else e finally são opcionais, enquanto o try deve vir acompanhado de um except. Também podemos ter varios except para um try.
----------------------------------------------------------------------------------------------------------------------------------
try: O "laboratório". Você coloca o código que corre risco de dar problema.

except: O "plano de contingência". Só roda se algo der errado no try.

else: O "caminho feliz". Só roda se o try foi um sucesso absoluto (zero erros).

finally: O "protocolo de encerramento". Roda sempre, não importa se deu erro ou não. É perfeito para fechar conexões com o banco de dados (PostgreSQL) ou fechar arquivos.
----------------------------------------------------------------------------------------------------------------------------------
LBYL (if) para: Validar formato, tamanho de string, se campos estão vazios (Sanitização).

EAFP (try) para: Operações de rede, leitura de arquivos, conversões de tipo (float/int) e qualquer interação com o Banco de Dados.

"O ideal para sistemas robustos é a validação híbrida: É o if para filtrar o que é previsível e try/except para capturar o imprevisível. Isso garante que o banco de dados receba dados limpos e que o sistema sobreviva a falhas de infraestrutura."
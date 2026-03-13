O Dicionario é a terceira variavel composta do Python. Pode ser decladara como: dados = dict(), ou dados = {    }
Diferente das outras estruturas que as buscas são feitas por indices, no dicionario temos as etiquetas ou chaves.
----------------------------------------------------------------------------------------------------------------------------------
Ex:
        dados = {"nome":"Pedro","idade":25}
        print(dados["nome"])
        print(dados["idade"])

Enquanto nas estruturas anterior as buscas eram realizadas pelos indices, aqui o uso das chaves facilitam as buscas e legibilidade do codigo
----------------------------------------------------------------------------------------------------------------------------------
Diferente das listas aqui não usamos o append, mas enserimos a nova chave + valor diretamente no dicionario.
Ex:
dados = {"nome": "Pedro","idade": 25}

dados["sexo"] = "m"

dados = {"nome": "Pedro","idade": 25,"sexo": "m"}

Para deletar usamos o del padrão e ensirimos a chave.

del dados[idade]

dados = {"nome": "Pedro","sexo": "m"}
----------------------------------------------------------------------------------------------------------------------------------
As estruturas de variaveis compostas não precisam fechar na mesma linha contando que a feche.

Ex:
        filme = {"titulo": "Star Wars",
                  "ano": 1977,
                  "diretor": "George Lucas"
                 }
----------------------------------------------------------------------------------------------------------------------------------
Comandos:

filme.values() Pega somente os valores.
filme.keys() Pega somente as Chaves.
filme.items() Pega os dois Chave e Valor
filme.copy() Copiar o valor assim como o [:] no entando dicionarios diferente das listas usam o .copy para copiar.
----------------------------------------------------------------------------------------------------------------------------------
O uso de loops também é possivel com essa estrutura.

Ex: for k, v in filme.items():
        print(f"O {k} é {v}.")

Usamos o metodo items para pegar chave e valor ao inves de enumarete nos dicionarios.
----------------------------------------------------------------------------------------------------------------------------------Também é possivel usar estruturas diferentes juntas: como o uso de dicionarios dentro de listas.

Ex: 
locadora = [{"titulo": "Star Wars", "ano": 1977, "diretor": "George Lucas"},
           {"titulo": "Avengers", "ano": 2012, "diretor": "Joss whendo"}, 
           {"titulo": "Matrix", "ano": 1999, "diretor": "Wachowski"}]

print(locadora[0]["ano"])  # Exibe 1977
print(locadora[2]["titulo"]) # Exibe Matrix
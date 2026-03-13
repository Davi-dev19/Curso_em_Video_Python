pessoas = {"nome": "Davi", "sexo": "masculino" , "idade": 19}
pessoas["nome"] = "Victor"

for k, v in pessoas.items():
    print(f"A chave é: {k} e valor: {v}") 

# Nos dicionarios podemos atribuir um novo valor a uma chave apenas a referenciando e atribuindo o novo valor diretamente nela.
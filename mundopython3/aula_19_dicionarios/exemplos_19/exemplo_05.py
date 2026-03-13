pessoas = {"nome": "Davi", "sexo": "masculino" , "idade": 19}
del pessoas["sexo"]

for k, v in pessoas.items():
    print(f"A chave é: {k} e valor: {v}") 
    
# Para manipular loops usando  dicionarios devemos usar os proprios metodos do dicionario. Sendo eles: .keys()  .values() .items()
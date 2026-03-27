def somar(* valores):
    soma = 0
    for num in valores:
        soma += num
    print(f"Somando os valores {valores} temos {soma} ")

somar(5, 2)
somar(2, 9, 4)
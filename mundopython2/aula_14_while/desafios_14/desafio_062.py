termo = int(input("Qual o termo? ")) 
razao = int(input("Qual a razão? "))
termo_atual = termo
contador = 0
total = 0
mais = 10

while mais != 0:
    total += mais 
    while contador < total:
        print(f"{termo_atual}", end=" --> ")
        termo_atual += razao
        contador+= 1
    print("Pausa")
    mais = int(input(f"""Digite a quantidade de termos que deseja ver a mais.
Caso deseje parar pressione [0].
Resposta: """))
    
print(f"{total} foram imprimidos.")

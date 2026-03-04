tuplas são variaveis compostas, enquanto variaveis guardam apenas 1 valor, tuplas podem guardar mais de 1 valor.
Ex:

    Variavel Simples                        Variavel Composta: Tupla            
    bebida = "agua"         bedidas = ("agua", "suco", "refrigerante", "chá", "café", "leite")
----------------------------------------------------------------------------------------------------------------------
Podemos acessar todos os valores da tupla apenas acessando a variavel bebidas, ou acessar um item em especifico de acordo com o indice: 0, 1, 2, 3, 4... O uso de fatiamento em variaveis compostas também é possivel.
Ex:

    print(bebidas)                   print(bebidas[0])                     print(bebidas[2:])
----------------------------------------------------------------------------------------------------------------------
As tuplas são imutaveis. Após definir os valores dentro de uma tupla, não é possivel fazer qualquer alteração, seja ela: remover um elemento, adicionar um elemento ou substituir um elemento por outro.
Elas utilizam o parenteses como sua estrutura de definição no inicio e final: ()
----------------------------------------------------------------------------------------------------------------------
Comandos:

len() Verifica o comprimento de uma String ou variavel composta: quantos elementos existem naquela estrutura.
tupla.index(item) Verifica em qual indice aquele item aperece primeiro.
tupla.count(item) Verifica quantas vezes aquele item aparece.
del(tupla) Deleta a tupla da memoria como se nunca tivesse existido.
.sorted(tupla) Ordena em ordem alfabetica.
----------------------------------------------------------------------------------------------------------------------------------Caso procure o indice de um elemento que não existe a linguarem irá gerar um erro. Portanto é sempre bom verificar antes da busca.
As funções tem como objetivo permitir a reutilização de uma parte do código, sem que eu precise o reescrever. Além disso facilita a manuntenção do código, pois como criamos pequenos blocos no código usando funções, podemos mexer somente nele quando necessario, fazendo com que não seja necessario mexer em varias partes do código. Quando criamos uma função, estamos criando comando personalizado.
----------------------------------------------------------------------------------------------------------------------------------
Para definir uma função no Python, usamos a estrutura: def, ela permite a criação de uma função, seguido do nome da função, parenteses e dois ponto: def função(): 
Definimos o que queremos dentro dela, usando a indentação.


Ex:     def mostrar_linha():
            print("----------------")


Dessa forma definimos uma função.
----------------------------------------------------------------------------------------------------------------------------------
Caso eu queira a chamar em algum momento do código, basta eu digitar o nome seguido do parenteses: função().

Ex:

mostrar_linha()
print("           SISTEMA DE ALUNOS           ")
mostrar_linha()
mostrar_linha()
print("        CADASTRO DE FUNCIONARIOS        ")
mostrar_linha()
mostrar_linha()
print("         ERRO DO SISTEMA         ")
mostrar_linha()
----------------------------------------------------------------------------------------------------------------------------------
Em funções também podemos utilizar passagem de parametros e argumentos, o parametro são as variaveis que vão dentro do parenteses na hora que definimos a função, ex: def função(Parametro_1, Parametro_2). Podemos ter mais de um parametro os separando por virgula.
Os argumentos definimos na hora que chamamos a função no programa principal, eles serão as entradas que ocuparão os espaços que definimos na função, ou seja, os parametros.


Ex:         def exibir_mensagem(msg):
                print("--------------------")
                print(msg)
                print("--------------------")
            

            mensagem("SISTEMAS DE ALUNOS")


No exemplo mostrado msg na hora que definimos a função é o parametro e "SISTEMAS DE ALUNOS" é o argumento passado na hora que chamamos a função. 
Obs: Quando definimos uma quantidade x de parametros na função, sempre que formos a chamar e passar os argumentos, a quantidade de argumentos passados devem ser iguais a quantidade de parametros definidos. No Python podemos misturar nos argumentos, argumentos explicitados e não explicitados, no entanto, os não explicitados devem vir primeiro, a parti do momento que explicitamos 1, devemos explicitar todos que vierem depois dele.
----------------------------------------------------------------------------------------------------------------------------------Argumentos não explicitados = Positional Arguments (Argumentos Posicionais).

Argumentos explicitados = Keyword Arguments (Argumentos de Palavra-chave ou Nomeados).

Tanto quando definimos explicitamente o parametro x = argumento y quanto quando usamos dicionarios, temos argumentos nomeados.
----------------------------------------------------------------------------------------------------------------------------------
Quando vamos alocar mais de um valor em um parametro, ou não sabemos quantos serão alocados, usamos o *

Ex:     def exibir_numeros(*num)


        exibir_numeros(2, 1, 7)


Dessa forma podemos alocar varios valores dentro de num. Dessa forma, num deixa de ser uma variavel simples e passa a ser uma tupla. Isso se chama empacotamento. Obs: Quando fazemos esse empacotamento o Python cria o espaço em formato de tupla.
---------------------------------------------------------------------------------------------------------------------------------
Para o desempacotamento, usamos o * na hora que chamamos a função, no desempacotamento ele pode ser usado em qualquer variavel composta, no entanto para dicionario devemos usar  dois asterisco ** , se não ele pega apenas a chave e as desempacotas como argumentos posicionais, podendo gerar um erro de resultado, ou um erro de tipo caso queiramos calcular algo. Queremos chave e valor, dessa forma desempacotamos os pares como argumentos nomeados.

* == chave
** == chave + valor
----------------------------------------------------------------------------------------------------------------------------------
Obs: É importante usar o * na hora de desempacotar estruturas compostas, pois se não ele aloca tudo de uma vez em um parametro, podemos ter duas situações possiveis. 1° caso a função esteja esperando os valores com o uso do empacotamento * e recebe apenas  argumento sem *, ele entende que aquilo é uma lista e coloca a lista dentro de uma tupla, caso espere mais de uma ele aloca tudo no primeiro parametro, gerando um erro, pedindo os argumentos dos parametros restantes. Qaundo usamos o * O asterisco atua como um operador de espalhamento (spread). Ele itera sobre a estrutura composta e passa cada elemento como um argumento individual para a função."
As listas compostas são listas dentro de listas.
Ex:  pessoas = [["João",34], ["Maria",25], ["Marco",19]]
----------------------------------------------------------------------------------------------------------------------------------
Como mostrado no exemplo anterior, existe um lista pessoas que dentro dela possui outras listas. Cada uma com um nome e idade de pessoas diferentes.
----------------------------------------------------------------------------------------------------------------------------------
As caracteristicas permanecem as mesmas de uma lista padrão, elas são: Mutaveis e cercadas por colchetes: [ ] As buscas seguem sendo por indices no entanto com 2 indices agora, sendo eles o indice da lista principal e os indices das listas dentro dela.

Ex:  pessoas = [["João",34], ["Maria",25], ["Marco",19]]
     print(pessoas[0][0])
----------------------------------------------------------------------------------------------------------------------------------
O exemplo anterior busca o indice 0 na lista principal e encontra a primeira lista, depois busca o indice 0 dentro dessa sublista, que nesse caso é "João" e o exibe.
----------------------------------------------------------------------------------------------------------------------------------
2° Ex: pessoas[1]

Já no segundo exemplo ele pega a lista do indice 1 e exibe ela toda: ["Maria",25]
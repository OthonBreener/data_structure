"""
* Função zip: é usada para unir duas listas, ela retorna um gerador com uma
tupla contendo os elementos da primeira e segunda lista.

* Função zip_longest: Pode ser utilizada para unir duas lista onde uma é maior
que a outra. Ela percorrer a maior e preenche com none os dados que faltam para
completar a interação na maior lista.
"""
from itertools import zip_longest, count

indice = count()

lista1 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
lista2 = ['SP', 'MG', 'BA']

lista3 = zip(indice, lista1, lista2)
lista4 = list(lista3) # retorno: [('São Paulo', 'SP'), ('Belo Horizonte', 'MG'), ('Salvador', 'BA')]

lista5 = zip_longest(lista1, lista2)
lista6 = list(lista5) # retorno: [('São Paulo', 'SP'), ('Belo Horizonte', 'MG'), ('Salvador', 'BA'), ('Monte Belo', None)]

# o parametro 'fillvalue' acrescenta um dado ao valor faltando para completar a interação pela lista maior
lista7 = zip_longest(lista1, lista2, fillvalue='Vazio')
lista8 = list(lista7) # retorno: [('São Paulo', 'SP'), ('Belo Horizonte', 'MG'), ('Salvador', 'BA'), ('Monte Belo', 'Vazio')]

######################### EXERCÍCIO #############################

"""
Considere duas listas de inteiros ou floats. Some os valores nas listas e retorne uma nova lista
com os valores somados. Se a lista for maior que a outra considere o tamanho da menor.
"""

from random import randint

my_first_list = [randint(0,100) for i in range(10)]
my_second_list = [randint(0,100) for i in range(8)]

soma_list = zip(my_first_list, my_second_list)
soma_final = [i[0] + i[1] for i in soma_list]

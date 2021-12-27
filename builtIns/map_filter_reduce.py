"""
map: recebe como argumento uma função e um interavel,
fazendo um mapeamento da função em cada item do iteravel.
"""

lista_1 = [1, 2, 3, 4, 5, 6, 7, 8]

nova_lista = map(lambda x: x*2, lista_1)
# retorna um objeto map, quando convertido: [2, 4, 6, 8, 10, 12, 14, 16]

dicionario_1 = [
    {'nome': 'p1', 'valor': 10},
    {'nome': 'p2', 'valor': 10.60},
    {'nome': 'p3', 'valor': 55.98},
    {'nome': 'p4', 'valor': 22},
    {'nome': 'p5', 'valor': 36},
    {'nome': 'p6', 'valor': 98},
    {'nome': 'p7', 'valor': 87},
    {'nome': 'p8', 'valor': 71},
    {'nome': 'p9', 'valor': 11},
    {'nome': 'p10', 'valor': 2},
    {'nome': 'p11', 'valor': 100}
]

def incrised_price(p):
    p['valor'] = round(p['valor'] * 1.05, 2)
    return p

novo_dict = map(incrised_price, dicionario_1)
print(list(novo_dict))

"""
filter: assim como map recebe uma função e um interavel como argumento,
        criando uma nova lista com os elementos que satisfazerem a condição
        da função.
"""

lista_2 = filter(lambda x: x > 5, lista_1)
print(list(lista_2))

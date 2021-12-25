from itertools import combinations, product, permutations, groupby

"""
Combinations - Não repete valor único e a ordem não importa
Permutations - Não repete valor único e a ordem importa
Product - Repete valor único e a ordem importa
"""
pessoas = ['Othon', 'Igor', 'João', 'Lais', 'Felipe', 'Henrique']

combi = [grupo for grupo in combinations(pessoas, 2)]
# combinations: retorna um gerador com todas as combinações possíveis para cada item da lista
#               sem repetir valores já combinados, independente da ordem.
# retorno:  [('Othon', 'Henrique'), ('Igor', 'João'), ('Igor', 'Lais'), ('Igor', 'Felipe'), ('Igor', 'Henrique'), ('João', 'Lais'),
 #          ('João', 'Felipe'), ('João', 'Henrique'), ('Lais', 'Felipe'), ('Lais', 'Henrique'), ('Felipe', 'Henrique')]

permut = [grupo for grupo in permutations(pessoas, 2)]
# retorna todas as combinações possíveis levando em conta a ordem

prod = [grupo for grupo in product(pessoas, repeat=2)]
# retorna todas as combinações possíveis repetindo valor com valor, ex: ('othon', 'othon')

"""
groupyby: módulo utilizada para agrupar chaves de um iterável.
          Recebe um iterável e uma chave, onde essa chave é um função
          que calcula um valor chave para cada elemento.
          Retorna a chave utilizada para agrupar e um iterador com os dados
          agrupados com chave. Geralmente necessita do objeto iterado já estar
          ordenado.
"""

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Lilian', 'nota': 'B'},
    {'nome': 'Larazo', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'A'},
    {'nome': 'Laura', 'nota': 'C'},
    {'nome': 'Livia', 'nota': 'B'},
    {'nome': 'Liz', 'nota': 'A'},
    {'nome': 'Luna', 'nota': 'B'},
    {'nome': 'Larissa', 'nota': 'C'},
    {'nome': 'Lucas', 'nota': 'B'},
]

ordened = lambda x: x['nota']

#ordena o dicionario pela nota
alunos.sort(key=ordened)

alunos_agrupados = groupby(alunos, ordened)
for key, value in alunos_agrupados:
    values = list(value)

    print(f'Agrupados pela nota: {key}')
    print(f'Quantidade de alunos que tiraram a nota {key}: {len(values)}')
    for aluno in values:
        print(aluno)
    print()

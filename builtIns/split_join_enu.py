"""
- Split: Dividi uma string
"""

string = 'Sempre que você quiser sair do planeta acesne para um disco voador, e diga que você tem uma certa urgência!'

lista = string.split(' ') # cria uma lista com os elementos sendo cada palavra da frase separadas por espaço.
lista.count('que') # retorna quantas vezes a palavra 'que' aparece na lista

lista_2 = string.split(',') # cria uma lista com cada elemento separado por virgula.

"""
- Join: Junta uma lista
"""

my_list = 'O Brasil é uma porcaria'.split()
my_join = ' '.join(my_list) #junta os elementos com um espaço para cada palavra

"""
- Enumerate: Enumera elementos de uma lista
"""

second_list = ['Ajax', 'Bitcoin', 'Atom', 'Shiba', 'Baby']

# enumerate cria uma tupla com o indicie e valor de cada elemento da lista
for indicie, value in enumerate(second_list):
    print(f'Este é o indicie: {indicie}')
    print(f'Este é o valor: {value}')
    print()

from math import log
import numpy as np
import matplotlib.pyplot as plt

"""
Notação Big-O
- É uma forma de comparar algoritmos de forma objetiva,
sem levar em consideração váriaveis como sistema operacional,
poder de processamento dos hardwares, linguagem de programação.

- Abra o terminal ipython e execute a função com
    %timeit soma_1(10)

Para ter uma visualização do tempo gasto para executara função.

"""

# O(n) função executa com n interações
def soma_1(n):
    soma = 0
    for i in range(n + 1):
        soma += i

    return soma

# O(3): função executada com 3 operações
def soma_2(n):
    return ((n + 1)*n)/2


def soma_3(n):
    return sum(range(n + 1))


def lista_1():
    lista = []
    for i in range(1000):
        lista += [i]

    return lista

def lista_2():
    return range(1000)


vetor = np.linspace(1, 10, 100)
labels = ['Constante', 'Logaritmo', 'Linear', 'Log Linear', 'Quadratica', 'Cubica', 'Exponencial']
big_o = [np.ones(vetor.shape), np.log(vetor), vetor, vetor * np.log(vetor), vetor ** 2, vetor ** 3, 2**vetor]

# rodar pelo jupyter para ver as imagens
plt.figure(figsize=(10,8))
for indicie, figure in enumerate(labels):
    plt.plot(vetor, big_o[indicie], label = figure)
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')


### Função Constante
def constante(vetor):
    """
    Função constante O(1) é executada uma única vez
    independente do valor de entrada.
    """
    print(vetor[0])

### Função Linear
def linear(vetor):
    """
    Uma função linear O(n) é executada n vezes,
    ela possui um loop que depende do valor de
    entrada para definir quando vezes o código será
    executado.
    """
    for i in vetor:
        print(i)

# Função Quadratica
def quadratica(vetor):
    """
    Uma função quadratica O(n^2) executa dois loops
    para cada item do dado de entrada.
    """
    for i in vetor:
        for j in vetor:
            print(i, j)

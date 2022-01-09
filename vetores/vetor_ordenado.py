"""
Vetores ordenados tem seus dados organizados na ordem
ascendente de valores-chave, ou seja, com o menor valor
no índice 0 e cada célula mantendo um valor maior que a
célula abaixo.
"""

import numpy as np

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            datas = [print(f'Indicie: {i}, Valor: {self.valores[i]}') for i in range(self.ultima_posicao + 1)]


    def pesquisa(self, valor):

        for i in range(self.capacidade):
            if self.valores[i] > valor:
                return -1

            if self.valores[i] == valor:
                return i

        return -1

    def inserir(self, valor):

        for i in range(self.capacidade):
            if self.valores[i] < valor and self.valores[i + 1] > valor:
                self.valores[i + 1] = valor

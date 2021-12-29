import numpy as np

class VetorNaoOrdenado:

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

    # O(1)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida!')

        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

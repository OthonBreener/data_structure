"""
Na programação POO, o termo factory (Fábrica) refere-se a uma classe
ou método que é responsável por criar objetos.

Vantagens:
    Permite criar um sistema com baixo acoplamento entre classes,
    pois oculta as classes que criam os objetos do código cliente.

    Facilita a adição de novas classes no código.

Desvantagens:
    Podem introduzir muitas classes no código.
"""

from abc import ABC, abstractmethod

#interface abstrata
class Veiculo(ABC):

    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class Carro(Veiculo):

    def buscar_cliente(self) -> None:
        print('Carro buscando cliente')


class Moto(Veiculo):

    def buscar_cliente(self) -> None:
        print('Moto buscando cliente')


#Factory
class VeiculoFactory:

    @staticmethod
    def get_veiculo(tipo: str) -> Veiculo:
        if tipo == 'carro':
            return Carro()

        if tipo == 'moto':
            return Moto()

        assert 0, 'Veiculo não existe'


#cliente
if __name__ == '__main__':
    veiculos = ['carro', 'moto', 'onibus']

    for i in veiculos:
        veiculo = VeiculoFactory.get_veiculo(i)
        veiculo.buscar_cliente()

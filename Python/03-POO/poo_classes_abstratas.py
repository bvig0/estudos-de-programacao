from abc import ABC, abstractmethod


class Produto(ABC):
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    # Property => acessa um método como atributo
    @property
    def preco_com_desconto(self):
        return self.preco * 0.9

    # Property abstrato => exige implementação nas classes filhas
    @property
    @abstractmethod
    def categoria(self):
        pass

    # Método abstrato => exige implementação nas classes filhas
    @abstractmethod
    def exibir_detalhes(self):
        pass


class Eletronico(Produto):
    @property
    def categoria(self):
        return "Eletrônico"

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} \nCategoria: {self.categoria} \nPreço original: R${self.preco:.2f} \nPreço com desconto: R${self.preco_com_desconto:.2f}")


class Livro(Produto):
    @property
    def categoria(self):
        return "Livro"

    def exibir_detalhes(self):
        print(f"Produto: {self.nome} \nCategoria: {self.categoria} \nPreço original: R${self.preco:.2f} \nPreço com desconto: R${self.preco_com_desconto:.2f}")



produto1 = Eletronico("Notebook", 3000)
produto2 = Livro("Python para Iniciantes", 100)

produto1.exibir_detalhes()
print("-------------------------")
produto2.exibir_detalhes()
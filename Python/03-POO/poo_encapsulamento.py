# Variaveis com nomes normais, representam dados publicos
# Variaveis que tenham "_" no começo do nome, representam dados privados
# Veja o exemplo abaixo:
class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor
            

conta = Conta(100)
conta.depositar(100)
print(conta._saldo)
conta.sacar(50)
print(conta._saldo, "\n------------------------")

# Property()

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Brian", 2006)
print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade}")
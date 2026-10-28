class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada")

    def correr(self):
        print("Andando com a bicicleta...")
        print("Vruummmmmm")

    # Uma das maneiras de chamar os items da classe
    # def __str__(self):
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.correr()
b1.buzinar()
b1.parar()

print("\nBicicleta Nº1:", b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
# Bicicleta.buzinar(b2) é a mesma coisa que b2.buzinar()
print(b2, "\n------------------")

# Construtores e Destrutores
class Cachorro:
    def __init__(self, nome, cor, acordado=True): 
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe...")

    def latir(self):
        print("Au au au")

c1 = Cachorro("Pipoca", "preto e branco")
c1.latir()
del c1




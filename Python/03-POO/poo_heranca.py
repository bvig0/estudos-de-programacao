# Herança Simples
class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carga):
        super().__init__(cor, placa, numero_rodas)
        self.carga = carga
    
    def esta_carregado(self):
        if self.carga:
            print("Estou carregado")
        else:
            print("Não estou carregado")


moto = Motocicleta("vermelha", "abc-1234", 2)
print(moto)

carro = Carro("prata", "xyz-0987", 4)
print(carro)

caminhao = Caminhao("branco", "gfd-8721", 8, False)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()
print("----------------------------------")

# Herança Múltipla
class Animal():
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

# Classes pais
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

# Classes netos
class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)

class Harpia(Ave):
    pass

gato = Gato(nro_patas=4, cor_pelo="preto")
print(gato)

perry = Ornitorrinco(nro_patas=3, cor_pelo="marrom", cor_bico="laranja")
print(perry)

harpia_brazuca= Harpia(nro_patas=2, cor_bico="cinza escuro")
print(harpia_brazuca)
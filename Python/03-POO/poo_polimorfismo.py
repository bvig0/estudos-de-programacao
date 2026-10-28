class Pardal:
    def fazer_som(self):
        print("Piu piu!")

class Gato:
    def fazer_som(self):
        print("Miau!")

class Robo:
    def fazer_som(self):
        print("Bip bop!")

# Uma única função que aceita QUALQUER coisa que saiba fazer_som
def interagir(objeto):
    objeto.fazer_som()

interagir(Pardal())  # Piu piu!
interagir(Gato())    # Miau!
interagir(Robo())    # Bip bop!
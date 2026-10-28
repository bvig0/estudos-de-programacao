# Variáveis de classe e Variáveis de instância
class Estudante:
    escola = "Python"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    print("--------------------")
    for obj in objs:
        print(obj)

aluno1 = Estudante("Pitoco", 1)
aluno2 = Estudante("Sox", 2)
aluno3 = Estudante("Pipoca", 3)

mostrar_valores(aluno1, aluno2, aluno3)

# Valor de Instância, ou seja, só altera um dos alunos
aluno2.escola = "Miaunês"
mostrar_valores(aluno1, aluno2, aluno3)

# Valor de Classe, ou seja, altera todos alunos
Estudante.escola = "Django"
mostrar_valores(aluno1, aluno2, aluno3)
print("-----------------------------------")
# Declarando
frutas = {"Laranja", "Morango", "Maracujá"}
print(frutas)
numeros = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
print(numeros)
letras = set("abacaxi") # {"b", "a", "c", "x", "i"}
print(letras)
carros = set(("palio", "gol", "celta", "palio")) # {"palio", "gol", "celta"}
print(carros)

# Conjunto NÃO permite elementos repetidos
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3}


# Percorrendo
for fruta in frutas:
    print(fruta)

# Verificando se um elemento existe
print("Laranja" in frutas)  # True
print("Banana" in frutas)   # False

# Tamanho
print(len(frutas))  # 3

# Conjuntos podem armazenar diferentes tipos
dados = {"Python", 10, 3.14, True}
print(dados)

# Conjunto vazio
conjunto = set()
print(conjunto)  # set()

# {} NÃO cria um conjunto vazio
dicionario = {}
print(dicionario)  # {}

# Conjunto não possui ordem definida
linguagens = {"Python", "Java", "C#"}
print(linguagens)

# Conjunto NÃO possui índice e fatiamento.
# Para acessar um elemento por índice ou fazer um fatiamento, é necessário transformar o conjunto em uma lista.

linguagensLista = list(linguagens) # Transformando um Conjunto em uma lista
print(linguagensLista[0])    # Acessando por índice
print(linguagensLista[0:2])  # Fatiamento
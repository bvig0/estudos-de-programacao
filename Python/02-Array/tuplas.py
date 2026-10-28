# Declarando
frutas = ("Laranja", "Morango", "Maracujá",) #Declarando com itens dentro da tupla
print(frutas)
letras = tuple("python")
print(letras)
numeros = tuple([1, 2, 3, 4])
print(numeros)
pais = ("Brasil",)
print(pais, "\n----------------------")

# Acessando
print(frutas[0]) # Laranja
print(frutas[2]) # Maracujá

#Indices negativos
print(frutas[-2]) # Morango
print(frutas[-1],  "\n----------------------") # Maracujá

# Aninhadas/Matrizes
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0]) # [1, "a", 2]
print(matriz[0][0]) # 1
print(matriz[1][2]) # 4
print(matriz[-1][-1],  "\n----------------------") # c

# Fatiamento
listaPalavra = ("p", "y", "t", "h", "o", "n")
print(listaPalavra[2:]) # ["t", "h", "o", "n"]
print(listaPalavra[:2]) # ["p", "y"]
print(listaPalavra[1:3]) # ["y", "t"]
print(listaPalavra[0:3:2]) # ["p", "t"]
print(listaPalavra[::]) # ["p", "y", "t", "h", "o", "n"]
print(listaPalavra[::-1], "\n----------------------") # ['n', 'o', 'h', 't', 'y', 'p']
# Fatiamento de tupla: tupla[início:fim:passo] permite selecionar uma parte da lista. 
# O início é incluído, mas o fim não. Os valores podem ser omitidos para usar o início/fim padrão, e um passo -1 percorre a lista ao contrário.

# Percorrer
carros = ("gol", "celta", "palio")
for carroItem in carros:
    print(carroItem)
# **Laço for: percorre cada item de uma lista, armazenando o item atual em uma variável temporária. 
# O código dentro do for é executado uma vez para cada item da lista.

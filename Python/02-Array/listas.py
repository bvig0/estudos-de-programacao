# Declarando
frutas = ["Laranja", "Morango", "Maracujá"] #Declarando com itens dentro
print(frutas)
frutas = [] #Declarando a lista vazia
print(frutas)
letras = list("python") #Transforma cada letra em um item de uma lista
print(letras)
numeros = list(range(10))
print(numeros)
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro, "\n----------------------")

# Acessando
frutas = ["Laranja", "Morango", "Maracujá"] #Declarando com itens dentro
print(frutas[0]) # Laranja
print(frutas[2]) # Maracujá

# Indice negativo
print(frutas[-1]) # Maracujá
print(frutas[-3], "\n----------------------") # Laranja

# Aninhadas/Matrizes
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]
print(matriz[0]) # [1, "a", 2]
print(matriz[0][0]) # 1
print(matriz[1][2]) # 4
print(matriz[-1][-1], "\n----------------------") # c
# Ou seja, o primeiro [] define a linha e o segundo a coluna/item especifico

# Fatiamento
listaPalavra = ["p", "y", "t", "h", "o", "n"]
print(listaPalavra[2:]) # ["t", "h", "o", "n"]
print(listaPalavra[:2]) # ["p", "y"]
print(listaPalavra[1:3]) # ["y", "t"]
print(listaPalavra[0:3:2]) # ["p", "t"]
print(listaPalavra[::]) # ["p", "y", "t", "h", "o", "n"]
print(listaPalavra[::-1], "\n----------------------") # ['n', 'o', 'h', 't', 'y', 'p']
# Fatiamento de listas: lista[início:fim:passo] permite selecionar uma parte da lista. 
# O início é incluído, mas o fim não. Os valores podem ser omitidos para usar o início/fim padrão, e um passo -1 percorre a lista ao contrário.

# Percorrer
carros = ["gol", "celta", "palio"]
for carroItem in carros:
    print(carroItem)
# Laço for: percorre cada item de uma lista, armazenando o item atual em uma variável temporária. 
# O código dentro do for é executado uma vez para cada item da lista.

# Enumerate
for indice, carroItem in enumerate(carros):
    print(f"{indice}: {carroItem}")
print("----------------------")

# Filtro 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares1 = []

for numero in numeros:
    if numero % 2 == 0:
        pares1.append(numero)
print(f"{numeros} \n{pares1}")

# Filtro 2
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)
lista = []

# APPEND - adiciona um elemento a lista
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista) # [1, 'Python', [40, 30, 20]]

# COPY - copia os elementos de uma lista para outra
listaCopia  = lista.copy()
listaCopia[0] = 9
print(f"{listaCopia} \n{id(lista), id(listaCopia)}")

# CLEAR - limpa a lista
lista.clear()
print(lista) # []

print("---------------------------")
# COUNT - conta o numero de vezes que o elemento é repetido
cores = ["vermelho", "azul", "verde", "azul", "verde", "azul"]
print(
    f"Vermelho: {cores.count("vermelho")} \nAzul: {cores.count("azul")} \nVerde: {cores.count("verde")}"
)
print(f"{cores.count(cores[1])} \n ---------------------------")
# EXTEND - adiciona uma LISTA a outra
linguagens = ["python", "js"]
linguagens2 = ["ts", "golang", "c"]
print(linguagens) # ["python", "js"]

linguagens.extend(["java", "csharp"])
print(linguagens) # ["python", "js", "java", "csharp"]

linguagens.extend(linguagens2)
print(linguagens) # ['python', 'js', 'java', 'csharp', 'ts', 'golang', "c"]
print("---------------------------")

# INDEX - mostra o indece da palavra especifica
print(linguagens.index("java"), linguagens.index("python")) # 2 e 0
print("---------------------------")

# POP - tira o ultimo elemento da lista ou o do index indicado
linguagens.pop() # c
linguagens.pop() # golang
linguagens.pop(0) # python
print(linguagens, "\n---------------------------") #['js', 'java', 'csharp', 'ts'] 

# REMOVE - tira elemento indicando ele em si
linguagens.remove("js")
print(linguagens, "\n---------------------------") # ['java', 'csharp', 'ts'] 

# REVERSE - inverte a ordem dos elementos da lista
linguagens.reverse()
print(linguagens, "\n---------------------------") # ['ts', 'csharp', 'java'] 

# SORT - Ordena a lista
linguagens = ['python', 'js', 'java', 'csharp', 'ts', 'golang', "c"]
linguagens.sort() # Ordem alfabetica
print(linguagens) # ['c', 'csharp', 'golang', 'java', 'js', 'python', 'ts']

linguagens.sort(reverse=True) # Ordem alfabetica invertida
print(linguagens) # 'ts', 'python', 'js', 'java', 'golang', 'csharp', 'c']

linguagens.sort(key=lambda x: len(x)) # Ordem crescente de caracter de cada elemento
print(linguagens, "\n---------------------------") # ['c', 'ts', 'js', 'java', 'python', 'golang', 'csharp']

# LEN - fala o tamanho das coisas
print(len(linguagens)) # 7
print(len(linguagens[3]), "\n---------------------------") # 4

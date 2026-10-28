# COUNT - conta o numero de vezes que o elemento é repetido
cores = ("vermelho", "azul", "verde", "azul", "verde", "azul",)
print(
    f"Vermelho: {cores.count("vermelho")} \nAzul: {cores.count("azul")} \nVerde: {cores.count("verde")}"
)
print(f"{cores.count(cores[1])} \n---------------------------")

# INDEX - mostra o indece da palavra especifica
linguagens = ('python', 'js', 'java', 'csharp', 'ts', 'golang', "c",)
print(linguagens.index("java"), linguagens.index("python")) # 2 e 0
print("---------------------------")

# LEN - fala o tamanho das coisas
print(len(linguagens)) # 7
print(len(linguagens[3])) # 4
caminho_lorem = "Python/06-Manipulaçao de Arquivos/lorem.txt"

# READ - Ler todo o conteúdo do arquivo de uma vez
arquivo = open(caminho_lorem, 'r')
print(arquivo.read())
arquivo.close()
print("==============================================================")

# READLINE - Ler uma linha do arquivo, se quiser ver outra tem que colocar o mesmo comando abaixo
arquivo = open(caminho_lorem, 'r')
print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())
arquivo.close()
print("==============================================================")

# READLINES - Lê todo o conteúdo e retorna ele como uma lista, com os itens sendo cada LINHA
arquivo = open(caminho_lorem, 'r')
print(arquivo.readlines())
arquivo.close()
print("==============================================================")

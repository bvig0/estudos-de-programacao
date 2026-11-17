caminho = "Python/06-Manipulaçao de Arquivos/teste.txt"
arquivo = open(caminho, 'w')

arquivo.write("Ola Mundo")
arquivo.writelines(['\nescrevendo\n', 'um\n', 'novo\n', 'texto'])
arquivo.close()

# WRITE -> Strings em váriaveis
# WRITELINES -> Strings em listas

# AMBAS vão escrever uma string em um arquivo de qualquer jeito, e ambas só vão pular linha se VOCÊ indicar.

nome = "Brian"
idade = 20
profissao = "Programador"
linguagem = "Python"

# 1- Estilo antigo:
# %s para valores strings. 
# %d para valores númericos inteiros. 
# %f para valores númericos decimais.
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))
# colocar a '%' no texto representando uma variavel, depois das apas coloque mais um '%' e abra o parenteses colocando as variaveis que deseja na ordem correja

print("---------------------------------------------------------------------------------------")
# 2- Método format:

# 2.1- Mesma lógica que o de cima, mas substitui o '%' por '{}'
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

# 2.2- Mesma lógica. Entretanto, eu posso colocar nas '{}' a posição correspondente a várivel, não precisando seguir mais a ordem colocada nos parenteses
print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))

# 2.3- Mesma lógica. Entretanto atribuo o a váriavel com um nome e escrevo o nome dentro das '{}'
print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

print("---------------------------------------------------------------------------------------")
# 3- f-string:
# Coloque a letra 'f' antes da string e apenas escreve o nome da variavel dentro das '{}'.
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}")
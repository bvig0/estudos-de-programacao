nome = "Brian Vigo de Oliveira"

print(nome[0])
print(nome[:9])
print(nome[10:])
print(nome[10:16])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])

# nome[inicio:fim:passo]
# inicio: posição onde a leitura começa
# fim: posição onde a leitura termina (não inclui essa posição)
# passo: quantidade de posições que serão puladas a cada leitura

# Exemplos:
# nome[3:]     -> começa na posição 3 e vai até o final
# nome[:5]     -> começa do início e vai até a 4
# nome[2:8]    -> começa na posição 2 e vai até a 7
# nome[2:10:2]  -> da posição 2 até a 9, pulando de 2 em 2
# nome[::2]    -> percorre toda a string pulando de 2 em 2
# nome[::-1]   -> percorre a string de trás para frente
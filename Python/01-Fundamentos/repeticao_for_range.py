# Número de 0 a 10
print("Números de 0 a 1:")
for numero in range(0, 11): 
    print(numero, end=" ")
print()

# Tabuada do 9
print("Tabuada do 9: ")
for numero in range(0, 91, 9): 
    print(numero, end=" ")
print("\n-------------------------------")

# Escolhendo um número para ver su tabuada
numeroTabuada = int(input("Digite um número para ver sua tabuada: "))
numeroMaximo = (numeroTabuada*10)+1
for numero in range(0, numeroMaximo, numeroTabuada):
    print(numero, end=" ")

# range(inicio, fim, passo)
# inicio: número inicial da sequência (inclui esse valor)
# fim: número onde a sequência para (NÃO inclui esse valor)
# passo: quanto será somado ou subtraído a cada repetição

# Exemplos:
# range(5)        -> 0, 1, 2, 3, 4
# range(1, 5)     -> 1, 2, 3, 4
# range(1, 10, 2) -> 1, 3, 5, 7, 9
# range(10, 0, -1)-> 10, 9, 8, 7, ..., 1
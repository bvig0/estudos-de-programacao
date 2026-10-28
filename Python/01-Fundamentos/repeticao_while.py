numero = int(input("Digite um número para ver sua tabuada: "))
contador = 0
while contador <= 10:
    resultado = numero * contador
    print(f"{numero} X {contador} = {resultado}")
    contador+=1
print("--------------------------------------------")

numero = int(input("Digite o número que o contador vai parar: "))
contador = 0
while contador <= numero:
    print(contador)
    contador+=1
    if contador == numero:
        print(contador)
        print(f"Contador chegou até o número escolhido ({numero})!")
        break


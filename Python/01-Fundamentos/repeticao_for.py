# Percorrer um texto
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
 
for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

# Explicando o for: No for, a variável antes do in recebe um valor por 
# vez. O for pega cada item de uma coleção (lista, string, range, etc.) e 
# atribui esse item à variável durante cada repetição do loop. 
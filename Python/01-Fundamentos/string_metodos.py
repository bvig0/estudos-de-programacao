texto1 = "pYtHoN"
texto2 = "  Python  "

print(texto1.upper()) # Deixa TUDO em maiusculo
print(texto1.lower()) # Deixa TUDO em minusculo
print(texto1.title()) # Deixa APENAS a primeira letra em maiusculo e o restante em minusculo

# Elimando espaços em branco em Strings
print(texto2.strip() + ".") # Tira qualquer espaço que nã esteja preenchido
print(texto2.lstrip() + ".") # Remove o espaço só da esquerda
print(texto2.rstrip() + ".") # Remove o espaço só da direita

# Junção e centralização
print(texto1.center(10, "#")) # Centraliza tudo, 1º para quantidade de caracter dentro da string e o 2º é a "borda" escolhida
print("-".join(texto1)) # Coloca a string que você quiser para ficar entre os caracteres da palavra
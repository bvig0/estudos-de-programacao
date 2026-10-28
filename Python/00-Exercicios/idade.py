# Leia o nome de uma pessoa e o ano de nascimento. Mostre a idade aproximada.

nome = input("Digite seu nome: ")
anoNasc = int(input("Digite o ano em que você nasceu: "))
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - anoNasc

print(f"Olá, {nome}! Sua idade é:", idade)
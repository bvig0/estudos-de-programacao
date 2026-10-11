# Declarando
pessoa1 = {"nome": "Fulano", "idade": 21}
pessoa2 = dict(nome="Ciclano", idade=23)
pessoa1["telefone"] = "00 98765-4321 " # {"nome": "Fulano", "idade": 21, "telefone": "00 98765-4321 "}

# Acessando
print(pessoa1) # {"nome": "Fulano", "idade": 21, "telefone": "00 98765-4321"}
print(pessoa1["nome"]) # Fulano
print(pessoa1["idade"]) # 21
print(pessoa1["telefone"], "\n------------") # 00 98765-4321

pessoa1["nome"] = pessoa2["nome"]
pessoa1["idade"] = 999
pessoa1["telefone"] = "00 55555-4321"
print(pessoa1,"\n------------") # {"nome": "Ciclano", "idade": 999, "telefone": "00 55555-4321"}

# Aninhado
contatos = {
    "fulano@gmail.com": {"nome": "Fulano", "telefone": "3333-2221"},
    "ciclano@gmail.com": {"nome": "Ciclano", "telefone": "3443-2121"},
    "pitoco@gmail.com": {"nome": "Pitoco", "telefone": "3343-1849"}
}

print(contatos) 
print(contatos["pitoco@gmail.com"]["telefone"]) # 3343-1849
print(contatos["pitoco@gmail.com"], "\n------------") # {'nome': 'Pitoco', 'telefone': '3343-1849'}

# Percorrer
for chave in contatos:
    print(chave, contatos[chave])

print()
for chave, valor in contatos.items():
    print(chave, valor)
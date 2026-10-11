usuarios = {
    "usuario1": {"id": 1, "nome": "Fulano", "idade": 21},
    "usuario2": {"id": 2, "nome": "Ciclano", "idade": 23},
    "usuario3": {"id": 3, "nome": "Pitoco", "idade": 10}
}

# COPY - copia os elementos de uma lista para outra
copia = usuarios.copy()
copia["usuario3"] = {"nome": "Pit"}
print(usuarios["usuario3"]) # {'id': 3, 'nome': 'Pitoco', 'idade': 10}
print(copia["usuario3"]) # {'nome': 'Pit'}

# CLEAR - limpa a lista
usuarios.clear()
print(usuarios, "\n------------") # {}

# FROMKEYS - criando chaves vazias ou com um valor padrão
print(dict.fromkeys(["nome", "telefone"])) # {'nome': None, 'telefone': None}
print(dict.fromkeys(["nome", "telefone"], "vazio"), "\n------------") # {'nome': 'vazio', 'telefone': 'vazio'}

# GET
# print(copia["chave"]) # KeyError
print(copia.get("chave")) # None
print(copia.get("chave", {})) # {}
print(copia.get("usuario1", {}), "\n------------") # {'id': 1, 'nome': 'Fulano', 'idade': 21}

# ITEMS
print(copia.items()) # dict_items([('usuario1', {'id': 1, 'nome': 'Fulano', 'idade': 21}), ('usuario2', {'id': 2, 'nome': 'Ciclano', 'idade': 23}), ('usuario3', {'nome': 'Pit'})])

print("\n", copia["usuario2"].items(), "\n------------") # dict_items([('id', 2), ('nome', 'Ciclano'), ('idade', 23)])

# KEYS - retorna apenas as chaves do dicionario
print(copia.keys(), "\n------------") # dict_keys(['usuario1', 'usuario2', 'usuario3'])

# POP - remove o elemento indicado
copia2 = copia.copy()
copia2.pop("usuario1")
print(copia2, "\n------------")

# POPITEM - não informa qual é a chave, removendo o ultimo item do discionario
copia2.popitem()
print(copia2, "\n------------")

# SETDEFAULT - não altera o valor se ele existe. Agora caso não exista, o mesmo é adicionado
contato = {"nome": "Pitoco", "telefone": "3333-2221"}

contato.setdefault("nome", "Duquesa")
print(contato) # {"nome": "Pitoco", "telefone": "3333-2221"}
contato.setdefault("idade", 10) 
print(contato, "\n------------") # {'nome': 'Pitoco', 'telefone': '3333-2221', 'idade': 10}

# UPDATE - nos deixa atualizar um dicionario com base em outro
contato.update({'nome': 'Sox', 'idade': 15, "email": "sox@gmail.com"})
print(contato, "\n------------") # {'nome': 'Sox', 'telefone': '3333-2221', 'idade': 15, 'email': 'sox@gmail.com'}

# VALUES - Retorna APENAS os valores do dicionario, não mostrando as chaves
print(copia.values(), "\n------------") # dict_values([{'id': 1, 'nome': 'Fulano', 'idade': 21}, {'id': 2, 'nome': 'Ciclano', 'idade': 23}, {'nome': 'Pit'}])

# IN - para ver se tem ou não um item dentro do dicionario
print("usuario1" in copia) # True
print("usuario99" in copia) # False
print("nome" in copia["usuario2"]) # True
print("telefone" in copia["usuario3"], "\n------------") # False

# DEL - remove o valor ou a chave com seus valores se indicado
del copia["usuario2"]["id"]
del copia["usuario3"]
print(copia)
# {'usuario1': {'id': 1, 'nome': 'Fulano', 'idade': 21}, 'usuario2': {'nome': 'Ciclano', 'idade': 23}}
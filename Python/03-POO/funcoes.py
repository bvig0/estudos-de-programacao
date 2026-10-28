# Declarando
def mensagem():
    print("Olá Mundo!")

def mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Executando
mensagem()
mensagem2("Pitoco")
mensagem3()
mensagem3("Sox")

# RETURN
def calcular_total(numeros):
    return sum(numeros);

def antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucecessor = numero + 1
    return antecessor, sucecessor

print("------------------\n", calcular_total([10, 20, 34])) # 64
print(antecessor_e_sucessor(10), "\n------------------") # (9, 11)

# Argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999,placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
print("-----------------------")

# Positional only
def criar_carro1(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro1("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# Keyword only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

# Keyword and positional only
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido

print("-----------------------")

def somar(a, b):
    return a + b

def exibit_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"resultado da operação: {a} + {b} = {resultado}")

exibit_resultado(9, 10, somar) # resultado da operação: 9 + 10 = 19

print("-----------------------")

# Escopo global
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))
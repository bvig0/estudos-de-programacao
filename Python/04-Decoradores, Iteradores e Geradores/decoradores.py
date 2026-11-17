# Passagem de parametro
def mensagem(nome):
    print('executando nome')
    return f"Oi {nome}"

def mensagem_longa(nome):
    print('executando mensagem longa')
    return f"Olá, tudo bem com você {nome}?"

def executar_mensagens(funcao, nome):
    print("executando função...")
    return funcao(nome)

print(executar_mensagens(mensagem, "Helio"))
print(executar_mensagens(mensagem_longa, "helio"))
print("---------------")

# Função interna
def principal():
    print("Executando a função principal")

    def funcao_interna():
        print("Executando a função interna")

    def funcao_interna2():
            print("Executando a função interna 2")

    funcao_interna2()
    funcao_interna()
principal()
print("---------------")

# Retornando função
def calculadora(operacao):
     def soma(a, b):
          return a + b

     def subtracao(a, b):
               return a - b
     
     def multiplicacao(a, b):
               return a * b
     
     def divisao(a, b):
               return a / b

     match operacao:
           case "+":
                 return soma
           case "-":
                 return subtracao
           case "*":
                 return multiplicacao
           case "/":
                 return divisao

op = calculadora("*")
print(op(5, 4))
print("---------------")

# Decorador
def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")
    return envelope

@meu_decorador
def funcao_exemplo():
      print("Olá mundo!")

# Maneira de chamar sem o @
teste = meu_decorador(funcao_exemplo)
teste()
print()

# Maneira de chamar com o @
funcao_exemplo()
print("---------------")

# Decorador com argumentos
def meu_decorador2(funcao):
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope

@meu_decorador2
def aprender(tecnologia):
      print(f"Estou aprendendo {tecnologia}")

aprender("Python")
print("---------------")

# Decorador com argumentos e duplicando
def duplicar(funcao):
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado

    return envelope

@duplicar
def aprender(tecnologia):
      print(f"Estou aprendendo {tecnologia}")
      return tecnologia.upper()

teste = aprender("Python")
print(teste)
print(aprender.__name__)
print("---------------")

# introspecção
import functools
def meu_decorador3(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope

@meu_decorador3
def aprender(tecnologia):
      print(f"Estou aprendendo {tecnologia}")

print(aprender.__name__)
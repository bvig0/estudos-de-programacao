# Leia dois números e mostre: a soma,a subtração, a multiplicação e a divisão.

# Já converto oque eu escrever em número inteiro
valorUm = int(input("Digite um valor: "))
valorDois = int(input("Digite mais um valor: "))

# Estou guardando os valores das contas nas variaveis
soma = valorUm + valorDois
subtracao = valorUm - valorDois
multiplicacao = valorUm * valorDois
divisao = valorUm / valorDois

print("")

# meio de código = processamento ou chamar uma variavel

# Formas de mostrar algo na tela:
# 1- Coloco o texto e depois a virgula para eu colocar qualquer meio de código
print("A soma é:", soma)

# 2- Escrevo "f" antes do texto, podendo agora colocar qualquer meio de código dentro do texto ao escrever dentro das chaves 
print(f"A subtração é: {subtracao}")

# 3- Ao colocar o "\n", ele pula para a próxima linha
print(f"A multiplicação é: {multiplicacao} \nA divisão é {divisao}")
# Leia o salário de um funcionário e mostre: o salário com 10% de aumento

nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário: "))

novoSalario = salario + (salario*10 / 100)

print(f"Parabéns {nome}! Você recebeu um aumento de 10%. \nSeu salário agora é: {novoSalario}")
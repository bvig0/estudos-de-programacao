# Leia a base e a altura de um retângulo e calcule: área e perímetro

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

area = base * altura
perimetro = 2 * (base + altura)

print("Área do retângulo:", area)
print("Perímetro do retângulo:", perimetro)
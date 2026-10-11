# Faça uma ficha para preencher: nome, idade, média e aprovado(true ou false).
# Aqui você vai apenas preencher a ficha para mostrar todos os tipos de variveis em Python

# Você pode colocar tanto o str quanto só o input para escrever textos. Input vem como padrão em String (Texto)
nome = str(input("Digite o nome do aluno: "))
idade = int(input("Digite a idade do aluno: "))
media = float(input("Digite a média do aluno: "))
aprovado = bool(input("O aluno foi aprovado? (se sim, digite qualquer coisa. Caso ao contrario, deixe vazio) "))

print(f"\nNome: {nome} \nIdade: {idade} \nMédia: {media} \nAprovado: {aprovado}")
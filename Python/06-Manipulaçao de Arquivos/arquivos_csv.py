import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
COLUNA_ID = 0
COLUNA_NOME = 1

# Escrevendo arquivos CSV
try:
    with open(ROOT_PATH / "usuarios.csv", "w", encoding='utf8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['id', 'nome'])
        escritor.writerow(['1', 'Pitoco'])
        escritor.writerow(['2', 'Sox'])
except IOError as exc:
    print(f"Erro ao criar o arquivo.\n {exc}")

# Lendo arquivos CSV 
try:
    with open(ROOT_PATH / "usuarios.csv", "r", encoding='utf8') as arquivo:
        leitor = csv.reader(arquivo)
        for index, row in enumerate(leitor):
            if index == 0:
                continue
            print(f'ID: {row[COLUNA_ID]} | NOME: {row[COLUNA_NOME]}')
except IOError as exc:
    print(f"Erro ao criar o arquivo.\n {exc}")


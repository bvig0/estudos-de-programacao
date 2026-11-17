from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
# abre e fecha o arquivo automaticamente
    with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

print("========================================")
try: 
    with open(ROOT_PATH/"arquivo-utf-8.txt", "w", encoding='utf8') as arquivo:
        arquivo.write("Aprendendo a manipular arquivos  utilizamdo python.")
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")

try: 
    with open(ROOT_PATH/"arquivo-utf-8.txt", "r", encoding='ascii') as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")
except UnicodeDecodeError as exc:
    print(exc)
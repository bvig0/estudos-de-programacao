import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent
# NÃO EXECUTE ESTE ARQUIVO SEM COMENTAR OS COMANDOS.
# POIS ELE VAI ACABAR CRIANDO O ARQUIVO, RENOMEANDO, REMOVENDO E TENTANDO MOVER ELE TODA HORA

# CRIOU UM NOVO DIRETORIO
os.mkdir(ROOT_PATH / 'novo-diretorio')

arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()

# RENOMEANDO UM ARQUIVO
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# REMOVENDO UM ARQUIVO
os.remove(ROOT_PATH / "alterado.txt")

# MOVENDO UM ARQUIVO PARA OUTRO DIRETORIO
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / 'novo-diretorio')

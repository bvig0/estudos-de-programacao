from datetime import date, datetime, timedelta

data = date(2006, 9, 2)
print(data)
print(data.today()) # Ano, mês e dia atual

#       Ano, Mês, Dia, Hora, Minuto, Segundo
data_hora = datetime(2006, 9, 2, 10, 30, 20)
print(data_hora)
print(f"Data: {datetime.now().date()}") # Pega apenas a data
print(f"Relógio: {datetime.now().time()}") # Pega apenas o relógio

# TIMEDELTA
tipo_carro = 'G' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} \nFicará pronto às: {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} \nFicará pronto às: {data_estimada}")
elif tipo_carro == 'G':
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} \nFicará pronto às: {data_estimada}")
else:
    print("Digite algo válido.")
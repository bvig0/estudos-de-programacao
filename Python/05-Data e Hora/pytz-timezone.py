import pytz
from datetime import datetime, timedelta, timezone

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data)
print(data2)

# Fazendo sem o PYTZ
data_oslo = datetime.now(timezone(timedelta(hours=1)))
data_sp = datetime.now(timezone(timedelta(hours=-3), "BR"))
print("---------\n", data_oslo)
print(data_sp)
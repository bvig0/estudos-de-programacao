from datetime import datetime
d = datetime.now()
mascaraPTBR = "%d/%m/%Y %H:%M"

# Formatando data e hora
print(d.strftime(mascaraPTBR)) # 11/11/2026 17:46

# Convertendo string para datetime
date_string = "02/09/2006 13:29"
data_convertida = datetime.strptime(date_string, mascaraPTBR)
print(data_convertida) # 2006-09-02 13:29:00 
print(type(data_convertida)) # <class 'datetime.datetime'>
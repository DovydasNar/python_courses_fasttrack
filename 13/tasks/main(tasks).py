#                                   1 task
import datetime
from datetime import datetime as d

dabartinis_laikas = d.today()

print(dabartinis_laikas)

metai = dabartinis_laikas.year
menuo = dabartinis_laikas.month
diena = dabartinis_laikas.day
valanda = dabartinis_laikas.hour
minute = dabartinis_laikas.minute
sekunde = dabartinis_laikas.second

print(f'Dabar yra: {valanda}:{minute}, {diena}-{menuo}-{metai}')


print('=================================================')

#                                   2 task

data_object = datetime.datetime(1995, 7, 14, 15, 30, 00)
print(data_object)

data_object2 = datetime.datetime(2023, 1,1)
print(data_object2)


print('=================================================')

#                                   3 task

data_2000 = datetime.datetime(2000, 1, 1)

data_from_today = (d.today() - data_2000).days

print(f'Praejo {data_from_today} dienu nuo 2000-01-01')


print('=================================================')

#                                   5 task

# datos_ivestis = input('Iveskite data formatu "YYYY-MM-DD": ')

# try:
#     objektas = datetime.datetime.strptime(datos_ivestis, "%Y-%m-%d")
#     print(f'Data ivesta formatu: {objektas}')
# except ValueError:
#     print('Ivestas neteisingas formatas')


print('=================================================')

#                                   6 task

objektas1 = datetime.datetime(2022, 12,31, 23,59,59)
print(objektas1)

objektas1_kitu_formatu = objektas1.strftime('%d/%m/%Y %H:%M:%S')

print(objektas1_kitu_formatu)
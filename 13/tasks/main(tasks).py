#                                   1 task

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


#                                   2 task


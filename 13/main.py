import datetime

print(type(datetime))  # <class 'module'>

# kreipiamės į funkcionalumą aprašytą datetime faile
# todėl kode 2 kartus kartojam datetime
# antrasis datetime yra kreipimasis į klasę
# .today() metodas sukuria šio laiko momento datos-laiko objektą
# rezultatas yra datetime.datetime objektas
dt_res = datetime.datetime.today()
print(dt_res)  # 2024-10-10 10:33:24.596796
print(type(dt_res))  # <class 'datetime.datetime'>


print('===========================================')

# patys sukuriam norimos datos ir laiko objektą
# pilnai užpildome datos ir laiko laukus
my_datetime = datetime.datetime(2011, 12, 31, 23, 59, 59)
print(my_datetime)  # 2011-12-31 23:59:59

# laiką paduoti nebūtina, užtenka datos
my_datetime = datetime.datetime(2000, 1, 1)
print(my_datetime)  # 2000-01-01 00:00:00

print('===========================================')


# mes galim daryti paskaičiavimus su datos-laiko objektais
# pvz gauti laiko skirtumą tarp datų
time_from_2000 = datetime.datetime.today() - my_datetime
print(time_from_2000)  # 9049 days, 13:43:49.111984

data_1996 = datetime.datetime(1996, 5, 23)

time_from_1996 = datetime.datetime.today() - data_1996

print(time_from_1996)

print('===========================================')

# ĮVESTIS
# sukursime savo ivesties formatą, naudojant kaukes - formato apibrėžimui
# ir str - įvesčiai
# .strptime - metodas naudoja kaukes, duomenų atpažinimui - https://strftime.org/
ivestis = "2020-02-11"
my_datetime = datetime.datetime.strptime(ivestis, "%Y-%m-%d")
print(my_datetime)

ivestis = "2020.02.15, 10:11:59"
my_datetime = datetime.datetime.strptime(ivestis, "%Y.%m.%d, %H:%M:%S")
print(my_datetime)

print('===========================================')

# IŠVESTIS,
# taip pačiai sudaroma kaukė, tačiau naudojamas kitas metodas,
# įvesties nepateikiama, naudojamas jau sukurtas datetime objektas
# strftime metodas
print(my_datetime)  # 2020-02-15 10:11:59
print(my_datetime.strftime("%d %m %Y"))  # 15 02 2020
print(my_datetime.strftime("%d %B %Y"))  # 15 February 2020

print('===========================================')

dabar = datetime.datetime.today()
mileniumas = datetime.datetime(2000, 1, 1)

# padarius atimtį datos-laiko iš datos-laiko, gaunamas kitas objektas
# laiko skirtumo(laiko tarpo) objektas datetime.timedelta
skirtumas = dabar - mileniumas
print(skirtumas)
print(type(skirtumas))  # <class 'datetime.timedelta'>

print('===========================================')


# laiko skirtumo objektą mes galim pridėti arba atimti iš datos laiko,
# gaudami kitą datetime objektą
# skaičiavimams dažniausiai patogiau sudaryti naują timedelta objektą,
# iškvietus jo klasę
skirtumas = datetime.timedelta(hours=1000)
print(skirtumas)
res = dabar + skirtumas
print(res)

skirtumas = datetime.timedelta(days=1000, hours=100, minutes=100)
print(skirtumas)
res = dabar - skirtumas
print(res)


print('===========================================')


# SVARBU! timedelta objekto laukai
print(skirtumas.days)  # dienomis
print(skirtumas.seconds)  # valandinė dalis atlikusi nuo dienų
print(skirtumas.seconds / 60 / 60)  # seconds valandomis

# VISOS laiko tarpo sekundės
sekundes = skirtumas.total_seconds()
print(sekundes)


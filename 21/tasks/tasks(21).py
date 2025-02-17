                                                                    # 1 uzduotis

from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///mokykla.db')
Base = declarative_base()


class Mokinys(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)

class Mokytojas(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)

Base.metadata.create_all(engine)



                                                    # 2 uzduotis


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

def iterpti_nauja_mokini():
    vardas = input('Iveskite mokinio varda: ')
    pavarde = input('Iveskite mokinio pavarde: ')
    klase = int(input('Iveskite mokinio klase: '))
    naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=klase)
    session.add(naujas_mokinys)
    session.commit()
    print(f'Mokinys {vardas} {pavarde} pridetas i sarasa. ')

def iterpti_nauja_mokytoja():
    vardas = input('Iveskite mokytojo varda: ')
    pavarde = input('Iveskite mokytojo pavarde: ')
    dalykas = input('Iveskite mokytojo destoma dalyka: ')
    naujas_mokytojas = Mokytojas(vardas=vardas, pavarde=pavarde, dalykas=dalykas)
    session.add(naujas_mokytojas)
    session.commit()
    print(f'Mokytojas {vardas} {pavarde} pridetas i sarasa. ')

def isvesti_visus_mokinius():
    mokiniai = session.query(Mokinys).all()
    print('Mokiniai:')
    for mokinys in mokiniai:
        print(f'Mokinys: {mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}')

def isvesti_visus_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    print('Mokytojai:')
    for mokytojas in mokytojai:
        print(f'Mokytojas: {mokytojas.vardas} {mokytojas.pavarde}, destomas dalykas: {mokytojas.dalykas}')


while True:
    print('Pasirinkite veiksma:')
    print('1 - Prideti mokini')
    print('2 - Prideti mokytoja')
    print('3 - Rodyti visus mokinius')
    print('4 - Rodyti visus mokytojus')
    print('5 - Iseiti is programos')

    pasirinkimas = input('Iveskite skaiciu: ')
    if pasirinkimas == '1':
        iterpti_nauja_mokini()
    elif pasirinkimas == '2':
        iterpti_nauja_mokytoja()
    elif pasirinkimas == '3':
        isvesti_visus_mokinius()
    elif pasirinkimas == '4':
        isvesti_visus_mokytojus()
    elif pasirinkimas == '5':
        print('Programa baigta')
        break
    else:
        print('Netinkamas skaicius')



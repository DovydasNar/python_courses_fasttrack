from sqlalchemy import Column, create_engine, String, Integer, REAL
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('sqlite:///mokyklos.db')
Base = declarative_base()


class Mokytojai(Base):
    __tablename__ = 'mokytojai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    dalykas = Column(String)
    atlyginimas = Column(Integer)


class Mokiniai(Base):
    __tablename__ = 'mokiniai'
    id = Column(Integer, primary_key=True)
    vardas = Column(String)
    pavarde = Column(String)
    klase = Column(Integer)
    vidurkis = Column(Integer)

Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()



mokinys1 = Mokiniai(
    vardas='Dovydas',
    pavarde='Narvilas',
    klase=11,
    vidurkis=8.5
)

mokinys2 = Mokiniai(
    vardas='Petras',
    pavarde='Petraitis',
    klase=12,
    vidurkis=7.2
)

mokinys3 = Mokiniai(
    vardas='Zivile',
    pavarde='Zivilaite',
    klase=12,
    vidurkis=9.3
)

mokinys4 = Mokiniai(
    vardas='Karolina',
    pavarde='Karolinaite',
    klase=7,
    vidurkis=7.6
)

mokinys5 = Mokiniai(
    vardas='Vidute',
    pavarde='Vidutaite',
    klase=12,
    vidurkis=9.8
)
#
# session.add(mokinys1)
# session.add(mokinys2)
# session.add(mokinys3)
# session.add(mokinys4)
# session.add(mokinys5)
#
# session.commit()
#
# print('Mokiniai prideti')








mokytojas1 = Mokytojai(
    vardas='Jonas',
    pavarde='Jonaitis',
    dalykas='Matematika',
    atlyginimas=1200
)

mokytojas2 = Mokytojai(
    vardas='Gytis',
    pavarde='Juzenas',
    dalykas='html, css, javascript',
    atlyginimas=3000
)

mokytojas3 = Mokytojai(
    vardas='Darius',
    pavarde='Daskevicius',
    dalykas='Python',
    atlyginimas=4000
)

mokytojas4 = Mokytojai(
    vardas='Jolanta',
    pavarde='Jolantiene',
    dalykas='Matematika',
    atlyginimas=1200
)

mokytojas5 = Mokytojai(
    vardas='Laima',
    pavarde='Laimaite',
    dalykas='Lietuviu kalba',
    atlyginimas=1000
)

mokytojas6 = Mokytojai(
    vardas='Irena',
    pavarde='Ireniene',
    dalykas='Biologija',
    atlyginimas=900
)

mokytojas8 = Mokytojai(
    vardas='Laima',
    pavarde='Laimaite',
    dalykas='Lietuviu kalba',
    atlyginimas=1000
)

# session.add(mokytojas1)
# session.add(mokytojas2)
# session.add(mokytojas3)
# session.add(mokytojas4)
# session.add(mokytojas6)
#
# session.commit()
#
# print('Prideta!')





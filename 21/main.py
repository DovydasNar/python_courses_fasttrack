
#   Duomenų bazės sukūrimas ir modelio aprašymas SQLALCHEMY

from sqlalchemy import Column, create_engine, Integer, String, Float
from sqlalchemy.orm import declarative_base

# Sukuriama arba prisijungiama prie SQLite duomenų bazės
engine = create_engine("sqlite:///projektai.db")
Base = declarative_base()

# Lentelės aprašymas
class Projektas(Base):
    __tablename__ = "projektai"
    id = Column(Integer, primary_key=True)
    pavadinimas = Column(String)
    kaina = Column(Float)

# Sukuriamos lentelės
Base.metadata.create_all(engine)
#

# ==================
# ==================


                                    # Duomenų įterpimas

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Naujo projekto sukūrimas
naujas_projektas = Projektas(pavadinimas="Tiltas", kaina=500000)
session.add(naujas_projektas)
session.commit()

#                                                    DUOMENU SKAITYMAS


visi_projektai = session.query(Projektas).all()
for projektas in visi_projektai:
    print(projektas.id, projektas.pavadinimas, projektas.kaina)


                                                    # Duomenų atnaujinimas

# Projekto paieška pagal ID ir atnaujinimas
projektas = session.get(Projektas, 1)
projektas.kaina = 600000
session.commit()

# Duomenų trynimas

# Projekto pašalinimas pagal ID
projektas = session.get(Projektas, 2)
session.delete(projektas)
session.commit()


# Paieška ir filtravimas

# Filtravimas pagal kainą
brangus_projektai = session.query(Projektas).filter_by(kaina=1000000).all()
for projektas in brangus_projektai:
    print(projektas.pavadinimas, projektas.kaina)

# Paieška pagal dalinį pavadinimo atitikimą
projektai = session.query(Projektas).filter(Projektas.pavadinimas.ilike("%Tiltas%"))
for projektas in projektai:
    print(projektas.pavadinimas, projektas.kaina)


#  Rikiavimas ir skaičiavimai

# Projektų rikiavimas pagal kainą
projektai = session.query(Projektas).order_by(Projektas.kaina).all()
for projektas in projektai:
    print(projektas.pavadinimas, projektas.kaina)


from sqlalchemy import func

# Projekto kainų suma
suma = session.query(func.sum(Projektas.kaina)).scalar()
print("Visų projektų suma:", suma)

# Taip pat galima atlikti sumavimus ir vidurkių skaičiavimus.
# Vidutinė kaina
vidurkis = session.query(func.avg(Projektas.kaina)).scalar()
print("Vidutinė kaina:", round(vidurkis))


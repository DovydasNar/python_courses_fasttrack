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
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

def iterpti_nauja_mokini():
    vardas = input('Iveskite mokinio varda: ')
    pavarde = input('Iveskite mokinio pavarde: ')
    klase = int(input('Iveskite mokinio klase: '))
    if not session.query(Mokinys).filter_by(vardas=vardas, pavarde=pavarde, klase=klase).first():
         naujas_mokinys = Mokinys(vardas=vardas, pavarde=pavarde, klase=klase)
         session.add(naujas_mokinys)
         session.commit()
         print(f'Mokinys {vardas} {pavarde} pridetas i sarasa. ')
         print('-' * 30)
    else:
        print('Mokinys jau egzistuoja.')
        print('-' * 30)

def iterpti_nauja_mokytoja():
    vardas = input('Iveskite mokytojo varda: ')
    print('-' * 30)
    pavarde = input('Iveskite mokytojo pavarde: ')
    print('-' * 30)
    dalykas = input('Iveskite mokytojo destoma dalyka: ')
    print('-' * 30)
    if not session.query(Mokytojas).filter_by(vardas=vardas, pavarde=pavarde, dalykas=dalykas).first():
         naujas_mokytojas = Mokytojas(vardas=vardas, pavarde=pavarde, dalykas=dalykas)
         session.add(naujas_mokytojas)
         session.commit()
         print(f'Mokytojas {vardas} {pavarde} pridetas i sarasa. ')
         print('-' * 30)
    else:
        print('Mokytojas jau egzistuoja.')
        print('-' * 30)

def isvesti_visus_mokinius():
    mokiniai = session.query(Mokinys).all()
    print('Mokiniai:')
    for mokinys in mokiniai:
        print(f'ID: [{mokinys.id}] Mokinys: {mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}')
        print('-' * 30)

def isvesti_visus_mokytojus():
    mokytojai = session.query(Mokytojas).all()
    print('Mokytojai:')
    for mokytojas in mokytojai:
        print(f' ID: [{mokytojas.id}], Mokytojas: {mokytojas.vardas} {mokytojas.pavarde}, destomas dalykas: {mokytojas.dalykas}')
        print('-' * 30)

def istrinti_mokini_pagal_id():
    mokinio_id = int(input('Iveskite mokinio ID numeri pagal kuri norite pasalinti mokini: '))
    mokinys = session.query(Mokinys).filter_by(id=mokinio_id).first()
    if mokinys:
        session.delete(mokinys)
        session.commit()
        print(f'Mokinys su ID: {mokinio_id} sekmingai istrintas.')
        print('-' * 30)
    else:
        print(f'Sistemoje tokio mokinio su ID: {mokinio_id} nera.')
        print('-' * 30)

def istrinti_mokytoja_pagal_id():
    mokytojo_id = int(input('Iveskite mokytojo ID numeri pagal kuri norite pasalinti mokytoja: '))
    mokytojas = session.query(Mokytojas).filter_by(id=mokytojo_id).first()
    if mokytojas:
        session.delete(mokytojas)
        session.commit()
        print(f'Mokytojas su ID: {mokytojo_id} sekmingai istrintas.')
        print('-' * 30)
    else:
        print(f'Sistemoje tokio mokytojo su ID: {mokytojo_id} nera.')
        print('-' * 30)


def istrinti_mokinius_12_klase():
    mokiniai_12_klase = session.query(Mokinys).filter_by(klase=12).all()
    if mokiniai_12_klase:
        for mokinys in mokiniai_12_klase:
            session.delete(mokinys)
            session.commit()
            print(f'Visi mokiniai baige 12 klasiu yra sekmingai istrinti.')
            print('-' * 30)
    else:
        print('Dvyliktoku nerasta.')


def rasti_mokini_pagal_varda():
    vardas = input('Iveskite mokinio varda pagal kuri norite rasti mokini: ')
    mokinys = session.query(Mokinys).filter_by(vardas=vardas).first()
    if mokinys:
        print(f'Rastas mokinys {mokinys.vardas} {mokinys.pavarde} klase: {mokinys.klase}')
    else:
        print(f'Mokinio vardu: {vardas} nerasta.')



def rasti_mokini_pagal_pirma_raide():
    mokiniai = session.query(Mokinys).filter(Mokinys.pavarde.ilike('P%')).all()
    if mokiniai:
        for mokinys in mokiniai:
            print(f'{mokinys.vardas} {mokinys.pavarde} klase: {mokinys.klase}')
    else:
        print('Mokiniu su pavardes pradzia P nerasta.')


def rasti_mokytoja_pagal_paskutine_raide():
    mokytojai = session.query(Mokytojas).filter(Mokytojas.pavarde.ilike('%s')).all()
    if mokytojai:
        for mokytojas in mokytojai:
            print(f'{mokytojas.vardas} {mokytojas.pavarde} destomas dalykas: {mokytojas.dalykas}')
    else:
        print('Mokytojas, kurio pavarde baigiasi s nerasta.')

def isvesti_mokinius_pagal_klase():
    mokiniai = session.query(Mokinys).order_by(Mokinys.klase).all()
    if mokiniai:
        print('Mokiniu sarasas pagal klase.')
        for mokinys in mokiniai:
            print(f'{mokinys.vardas} {mokinys.pavarde}, klase: {mokinys.klase}')
    else:
        print('Mokiniu nerasta.')

def mokiniu_skaicius_klaseje():
    rezultatas = session.query(Mokinys.klase, func.count(Mokinys.id)).group_by(Mokinys.klase).all()
    if rezultatas:
        print('Mokiniu skaicius kiekvienoje klaseje.')
        for klase, mokiniu_sk in rezultatas:
            print(f'Klaseje: {klase} mokiniu skaicius: {mokiniu_sk}')
    else:
        print('Mokiniu nerasta.')



while True:
    print('Pasirinkite veiksma:')
    print('1 - Prideti mokini')
    print('2 - Prideti mokytoja')
    print('3 - Rodyti visus mokinius')
    print('4 - Rodyti visus mokytojus')
    print('5 - Istrinti mokini pagal ID')
    print('6 - Istrinti mokytoja pagal ID')
    print('7 - Istrinti mokinius baigusius 12 klasiu')
    print('8 - Rasti mokini pagal varda')
    print('9 - Rasti mokini kurio pavarde prasideda is P raides')
    print('10 - Rasti mokytoja kurio pavarde baigiasi s raide')
    print('11 - Rikiuoti mokinius pagal klases')
    print('12 - Mokiniu skaicius pagal klase')
    print('13 - Iseiti is programos')

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
        istrinti_mokini_pagal_id()
    elif pasirinkimas == '6':
        istrinti_mokytoja_pagal_id()
    elif pasirinkimas == '7':
        istrinti_mokinius_12_klase()
    elif pasirinkimas == '8':
        rasti_mokini_pagal_varda()
    elif pasirinkimas == '9':
        rasti_mokini_pagal_pirma_raide()
    elif pasirinkimas == '10':
        rasti_mokytoja_pagal_paskutine_raide()
    elif pasirinkimas == '11':
        isvesti_mokinius_pagal_klase()
    elif pasirinkimas == '12':
        mokiniu_skaicius_klaseje()
    elif pasirinkimas == '13':
        print('Programa baigia savo darba')
        break
    else:
        print('Netinkamas skaicius')






# One-to-Many ryšys
#
# Vienas-daugeliui (One-to-Many) ryšys reiškia, kad viena lentelės eilutė gali turėti kelias susijusias eilutes kitoje lentelėje. Pavyzdžiui, viena komanda (Team) gali turėti daug programuotojų (Coder).
#
# Lentelių kūrimas

from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine("sqlite:///one_to_many.db")
Base = declarative_base()
#
# class Coder(Base):
#     __tablename__ = "coder"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(20))
#     last_name = Column(String(20))
#     age = Column(Integer)
#     xp_years = Column(Integer)
#     team_id = Column(Integer, ForeignKey("team.id"))
#     team = relationship("Team", back_populates="coders")
#
# class Team(Base):
#     __tablename__ = "team"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     description = Column(String)
#     coders = relationship("Coder", back_populates="team")
#
# Base.metadata.create_all(engine)
#
# # Ryšio naudojimas su SQLAlchemy
#
# from sqlalchemy.orm import sessionmaker
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# team_row = Team(name="DevOps")
# coder_row = Coder(first_name="Romas", last_name="Adomaitis", age=35, team=team_row)
# coder_row2 = Coder(first_name="Adomas", last_name="Adomaitis", age=25, team=team_row)
#
# session.add(team_row)
# session.commit()


# Many-to-Many ryšys

from sqlalchemy import Table, Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


engine = create_engine('sqlite:///many_to_many.db')
Base = declarative_base()

# - STEP 1: Create tables
association_table = Table('association', Base.metadata,
                          Column('coder_id', Integer, ForeignKey('coder.id')),
                          Column('skill_id', Integer, ForeignKey('skill.id')))


class Coder(Base):
    __tablename__ = 'coder'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    xp_years = Column(Integer)

    skills = relationship('Skill', secondary=association_table, back_populates='coders')


class Skill(Base):
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    technology = Column(String)

    coders = relationship('Coder', secondary=association_table, back_populates='skills')


Base.metadata.create_all(engine)

# - Step 2: Create records
Session = sessionmaker(bind=engine)
session = Session()

# skill_row1 = Skill(technology='Python')
# skill_row2 = Skill(technology='Java')
# skill_row3 = Skill(technology='Django')
# skill_row4 = Skill(technology='PostgreSQL')
# skill_row5 = Skill(technology='Google Cloud')
#
# coder_row1 = Coder(
#     first_name='Romas',
#     last_name='Adomaitis',
#     age=35,
#     skills = [
#         skill_row1, skill_row3, skill_row4
#     ]
# )
#
# coder_row2 = Coder(
#     first_name='Adomas',
#     last_name='Adomaitis',
#     age=25,
#     skills=[
#         skill_row1, skill_row2, skill_row5, skill_row4
#     ]
# )
#
# coder_row3 = Coder(
#     first_name='Tomas',
#     last_name='Adomaitis',
#     age=25,
#     skills = [
#         skill_row1, skill_row5
#     ]
# )
#
# session.add(coder_row1)
# session.add(coder_row2)
# session.add(coder_row3)
#
# session.commit()

# - STEP 3 - print created data
all_coders = session.query(Coder).all()
for row in all_coders:
    print(row.first_name, row.last_name, row.age, [s.technology for s in row.skills])

print('-' * 39)

all_skills = session.query(Skill).all()
for row in all_skills:
    print(row.technology, [f'{c.first_name} {c.last_name} {c.age}' for c in row.coders])


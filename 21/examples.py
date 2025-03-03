from models import Projektas, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()


def print_all_records():
    print("\nAll projects:")
    for row in session.query(Projektas).all():
        print(row)
    print('-' * 30)


def get_aggregates():
    total = session.query(func.sum(Projektas.kaina)).scalar()
    average = session.query(func.avg(Projektas.kaina)).scalar()
    print(f"Total project cost: {total}")
    print(f"Average project cost: {average:.2f}")
    print('-' * 30)


def get_most_expensive_project():
    project = session.query(Projektas).order_by(Projektas.kaina.desc()).first()
    if project:
        print(f"Most expensive project: {project}")
    else:
        print("No projects found.")
    print('-' * 30)


def filter_projects_by_name(name):
    print(f"Projects with name '{name}':")
    projects = session.query(Projektas).filter(Projektas.pavadinimas.ilike(f'%{name}%')).all()
    if projects:
        for project in projects:
            print(project)
    else:
        print("No matching projects found.")
    print('-' * 30)


def add_project(name, price):
    project = Projektas(pavadinimas=name, kaina=price)
    session.add(project)
    session.commit()
    print(f"Added new project: {project}")
    print('-' * 30)


def search_project(name, price=None):
    query = session.query(Projektas).filter_by(pavadinimas=name)
    if price:
        query = query.filter_by(kaina=price)

    try:
        project = query.one()
        print(f"Found project: {project}")
    except NoResultFound:
        print("No project found.")
    except MultipleResultsFound:
        print("Multiple projects found.")
    print('-' * 30)


def delete_project_by_id(project_id):
    project = session.get(Projektas, project_id)
    if project:
        session.delete(project)
        session.commit()
        print(f"Deleted project with ID: {project_id}")
    else:
        print("Project not found.")
    print('-' * 30)

print_all_records()
get_aggregates()
get_most_expensive_project()
filter_projects_by_name("Super")
search_project("Project2")
delete_project_by_id(2)
print_all_records()

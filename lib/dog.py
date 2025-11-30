from models import Dog, Base
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    """
    Create all tables for the given declarative base in the given engine.
    """
    base.metadata.create_all(engine)

def save(session, dog):
    """Add a Dog instance to the database."""
    session.add(dog)
    session.commit()

def get_all(session):
    """Return all Dog records."""
    return session.query(Dog).all()

def find_by_name(session, name):
    """Return the first Dog record with the given name."""
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    """Return the Dog record with the given id."""
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    """Return the first Dog record matching name and breed."""
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, breed):
    """Update the breed of the given dog and commit."""
    dog.breed = breed
    session.commit()

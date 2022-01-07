import os
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, DateTime, create_engine
from datetime import datetime

# setting up the path for the db file
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///"+os.path.join(BASE_DIR, 'site.db')

# base class from which all models are inherited
Base = declarative_base()

# setting up the engine required for querying and interacting with the db
engine =create_engine(connection_string, echo=True)

# session object
Session = sessionmaker()

# creating a table model
class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    # object representation method
    def __repr__(self):
        return f'User username={self.username} email={self.email} date_created={self.date_created}'

# new_user = User(username='John Doe', email='johndoe@test.com')
# print(new_user)

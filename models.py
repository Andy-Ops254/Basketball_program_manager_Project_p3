from sqlalchemy import String, Integer, DateTime, Float, Boolean
from sqlalchemy import Column, ForeignKey, create_engine, Index, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///basketball_manager.db') #used to translate sql to python n vice versa

Base = declarative_base() #used to create most basic rep. of tables
Session =sessionmaker(bind=engine)
session = Session()

class Team (Base):
    __tablename__ = 'teams'
    __table_args__ =(
        UniqueConstraint('name',
                        name='unique_name'),
            Index('index_team_name', 'name'))


    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    city = Column(String())

    managers = relationship ('Manager', backref=backref('team', uselist = False)) #connection to managers
    players = relationship('Player' ,backref=backref('team')) #connection to players

    def __repr__(self):
        return f"Team {self.id}, " +\
        +f"Team {self.name}," +\
        +f"Team {self.city}"


class Manager (Base):
    __tablename__ = 'managers'
    __tableargs__ = (
        Index('index_First_name', 'First_name'),
    )

    id = Column(Integer, primary_key=True)
    First_name = Column(String(20))
    Last_name = Column(String(20))
    email = Column(String())
    Hire_Date = Column(DateTime() ,default= datetime.now)

    Team_id = Column(Integer(), ForeignKey ('teams.id'))

    def __repr__(self):
        return f"Manager {self.id}, " +\
        f"Manager {self.First_name}," +\
        f"Manager {self.Last_name}," +\
        f"Manager {self.email}," +\
        f"Manager {self.Hire_Date}," +\
        f"Mnager {self.Team_id}"


class Player (Base):
    __tablename__ = 'players'
    __tableargs__ = (
        Index('index_last_name', 'last_name'),
        Index('index_jersey_number', 'jersey_number')
    )

    Index('index_last_name', 'last_name')
    Index('index_jersey_number', 'jersey_number')

    id = Column(Integer, primary_key = True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    age = Column(Integer())
    height = Column(String())
    position = Column(String())
    jersey_number= Column(Integer())
    signing_date= Column(DateTime(), default=datetime.now)

    Team_id = Column(Integer(), ForeignKey ('teams.id'))

    def __repr__(self):
        return f"Player {self.id}, " +\
        f"Player {self.first_name}," +\
        f"Player {self.last_name}," +\
        f"Player {self.age}," +\
        f"Player {self.height}," +\
        f"Player {self.position}," +\
        f"Player {self.jersey_number}," +\
        f"Player {self.signing_date}," +\
        f"Player {self.Team_id}"





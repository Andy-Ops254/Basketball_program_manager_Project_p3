from sqlalchemy import String, Integer, DateTime, Float, Boolean
from sqlalchemy import Column, ForeignKey, create_engine, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref
from datetime import datetime

engine = create_engine('sqlite:///basketball_manager.db') #used to translate sql to python n vice versa

Base = declarative_base() #used to create most basic rep. of tables

class Team (Base):
    __tablename__ = 'teams'
    # __table_args__ =(
    #     UniqueConstraint('name',
    #                     name='unique_name')
    # )

    id = Column(Integer, primary_key = True)
    name = Column(String(20))
    city = Column(String())

    managers = relationship ('Manager', backref=backref('team', uselist = False)) #connection to managers
    players = relationship('Player' ,backref=backref('team')) #connection to players

    def __repr__(self):
        return f"Team {self.id}: " \
        +f"Team {self.name}:" \
        +f"Team {self.city}"


class Manager (Base):
    __tablename__ = 'managers'

    id = Column(Integer, primary_key=True)
    First_name = Column(String(20))
    Last_name = Column(String(20))
    email = Column(String())
    Hire_Date = Column(DateTime() ,default= datetime.now)

    Team_id = Column(Integer(), ForeignKey ('teams.id'))

    def __repr__(self):
        return f"Manager {self.id}: " \
        +f"Manager {self.First_name}:" \
        +f"Manager {self.Last_name}:" \
        +f"Manager {self.email}:" \
        +f"Manager {self.Hire_Date}:" \
        +f"Mnager {self.Team_id}"


class Player (Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key = True)
    First_name = Column(String(20))
    Last_name = Column(String(20))
    Age = Column(Integer())
    Height = Column(String())
    Position = Column(String())
    Jersey_Numbet= Column(Integer())
    Signing_Date= Column(DateTime(), default=datetime.now)

    Team_id = Column(Integer(), ForeignKey ('teams.id'))





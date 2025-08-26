from sqlalchemy import String, Integer, DateTime, Float, Boolean
from sqlalchemy import Column, ForeignKey, create_engine, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

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

    def __repr__(self):
        return f"Team {self.id}: " \
        +f"Team {self.name}:" \
        +f"Team {self.city}"

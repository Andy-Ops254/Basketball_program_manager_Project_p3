from sqlalchemy import String, Integer, DateTime, Float, Boolean
from sqlalchemy import column, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///basketball_manager.db') #used to translate sql to python n vice versa

Base = declarative_base() #used to create most basic rep. of tables


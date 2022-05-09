from sqlalchemy import MetaData, create_engine, Column
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
engine = create_engine('sqlite:///user_database', connect_args={'check_same_thread': False}, echo=False)
Base = declarative_base();


class City(Base):
    __tablename__='city'
    city_id= Column()

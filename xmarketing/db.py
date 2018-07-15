# -*- coding: UTF-8 -*-

import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, DATETIME, BOOLEAN
from xmarketing import app

print("Connecting " + app.config['DATABASE_URI'])

# echo=False
engine = create_engine(app.config['DATABASE_URI'],pool_recycle=3600)

Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

class Visitor(Base):
    __tablename__ = 'visitor'
    """docstring for Visitor."""
    id = Column(BIGINT(20), primary_key=True)
    visitor_name = Column(VARCHAR(255), nullable=False)
    company_name = Column(VARCHAR(255))
    title = Column(VARCHAR(255))
    email = Column(VARCHAR(255), nullable=False)
    website = Column(VARCHAR(255))
    address = Column(VARCHAR(255))
    telephone = Column(VARCHAR(255))
    mobile = Column(VARCHAR(255))
    prefered_products = Column(VARCHAR(255))  # EPCalin EPColor Both(Mutiple choice)
    application = Column(VARCHAR(255))         # manually input
    preference = Column(VARCHAR(255))           # Mutiple choice
    pic_path = Column(VARCHAR(255))
    is_sent = Column(BOOLEAN, default=False)
    create_time = Column(DATETIME)

Base.metadata.create_all(engine)

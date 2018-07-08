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

Session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

class Visitor(Base):
    __tablename__ = 'visitor'
    """docstring for Visitor."""
    id = Column(BIGINT(20), primary_key=True)
    visitor_name = Column(VARCHAR(255))
    company_name = Column(VARCHAR(255))
    email = Column(VARCHAR(255))
    website = Column(VARCHAR(255))
    address = Column(VARCHAR(255))
    telephone = Column(VARCHAR(255))
    mobile = Column(VARCHAR(255))
    fax = Column(VARCHAR(255))
    preference = Column(VARCHAR(255))
    is_sent = Column(BOOLEAN)
    create_time = Column(DATETIME)

Base.metadata.create_all(engine)

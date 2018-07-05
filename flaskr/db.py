# -*- coding: UTF-8 -*-

import datetime
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import VARCHAR, BIGINT, LONGTEXT, INTEGER, DATETIME
from donato import app

# echo=False
engine = create_engine(app.config['DATABASE_URI'],pool_recycle=3600)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class Visitor(object):
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
    create_time = Column(DATETIME)

Base.metadata.create_all(engine)

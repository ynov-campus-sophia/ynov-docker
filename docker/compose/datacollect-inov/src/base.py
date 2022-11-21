#!/usr/bin/python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

connection = 'postgresql://{}:{}@{}:{}/{}'.format(os.getenv('DB_USER', 'executor'), os.getenv('DB_PASSWORD', '123456'),os.getenv('DB_HOST', 'pg'),os.getenv('DB_PORT', 5432),os.getenv('DB_NAME', 'crypto-executor'))
engine = create_engine(connection)
Session = sessionmaker(bind=engine)

Base = declarative_base()
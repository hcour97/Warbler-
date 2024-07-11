"""Seed database with sample data from CSV Files."""

from csv import DictReader
from app import db
from models import User, Message, Follows
import logging


db.drop_all()
db.create_all()

with open('generator/users.csv') as users:
    logging.info('Inserting users...')
    db.session.bulk_insert_mappings(User, DictReader(users))

with open('generator/messages.csv') as messages:
    logging.info('Inserting messages...')
    db.session.bulk_insert_mappings(Message, DictReader(messages))

with open('generator/follows.csv') as follows:
    logging.info('Inserting follows...')
    db.session.bulk_insert_mappings(Follows, DictReader(follows))

db.session.commit()
logging.info('Database seeding completed!')

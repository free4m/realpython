import os
from config import db
from models import Person


# Data to initialize the database
PEOPLE = [
    {'fname': 'Doug', 'lname': 'Farrell'},
    {'fname': 'Kent', 'lname': 'Brockman'},
    {'fname': 'Bunny','lname': 'Easter'},
]


# Delete database file if it already exists
if os.path.exists('people.db'):
    os.remove('people.db')


# Create the database
db.create_all()


# Iterate over PEOPLE and populate the database
for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'])
    db.session.add(p)


db.session.commit()

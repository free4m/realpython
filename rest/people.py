from datetime import datetime
from flask import make_response, abort
from config import db
from models import (
    Person,
    PersonSchema,
    Note,
    NoteSchema
)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


# Data to serve with our API
PEOPLE = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}


#  Create a handler for our read (GET) people
def read_all():
    """
    This function will respond to a request for /api/people
    with the complete list of people

    :return: sorted list of people
    """
    # create the list of people from our data
    people = Person.query.order_by(Person.lname).all()

    # serialize the data from the response
    person_schema = PersonSchema(many=True)
    data = person_schema.dump(people)
    return data


def read_one(person_id):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people

    :param person_id:   last name of person to find
    :return:        person matching last name
    """
    # Get the person requested
    person = Person.query.filter(Person.person_id == person_id).outerjoin(Note).one_or_none()

    # Did we find a person?
    if person is not None:
        # Serialize the data for a response
        person_schema = PersonSchema()
        return person_schema.dump(person)

    # we did not find a person
    else:
        abort(404, f'Person not found for ID: {person_id}')


def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    existing_person = Person.query.filter(Person.fname == fname, Person.lname == lname).one_or_none()

    # Can we insert this person?
    if existing_person is None:
        # Create a person instance using the passed in person
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session)

        # add the person to the db
        db.session.add(new_person)
        db.session.commit()

        # serialize and return the newly created person in the response
        return schema.dump(new_person), 201

    # can't create this person
    else:
        abort(409, f'Person {fname} {lname} already exists!')


def update(person_id, person):
    """
    This function updates an existing person in the people structure

    :param person_id:   ID of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Get the person requested from the db into session
    update_person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # try to find an existing person with the same name as the update
    fname = person.get("fname")
    lname = person.get("lname")

    existing_person = (Person.query.filter(Person.fname == fname).filter(Person.lname == lname).one_or_none())

    # are we trying to find a person that does not exist?
    if update_person is None:
        abort(404, f"Person for ID {person_id} not found.")

    # would our update create a duplicate of another person already existing?
    elif (existing_person is not None and existing_person.person_id != person_id):
        abort(409, f"Person {fname} {lname} already exists.")

    # no? then update
    else:
        # turn the person into a db object
        schema = PersonSchema()
        update = schema.load(person, session=db.session)

        # set the ID of the person we want to update
        update.person_id = update_person.person_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return the updated person in the response
        data = schema.dump(update_person)

        return data, 200


def delete(person_id):
    """
    This function deletes a person from the people structure

    :param person_id:   ID of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # get the person requested
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # did we find the person?
    if person is not None:
        db.session.delete(person)
        db.session.commit()
        return make_response(f"Person {person_id} deleted.")

    # did not find that person
    else:
        abort(404, f"Person for {person_id} not found.")
from flask import make_response, abort
from config import db
from models import Person, Note, NoteSchema


def read_all():
    """
    refers to /api/people/notes

    :return: json list of all notes for all people
    """
    # query for the notes
    notes = Note.query.order_by(db.desc(Note.timestamp)).all()

    # serialize the list
    note_schema = NoteSchema(many=True, exclude=["person.notes"])
    data = note_schema.dump(notes)
    return data


def read_one(person_id, note_id):
    """
    /api/people/{person_id}/notes/{note_id}

    :param person_id:
    :param note_id:
    :return: one matching note
    """
    # query the database for the note
    note = (
            Note.query.join(Person, Person.person_id == Note.person_id)
            .filter(Person.person_id == person_id)
            .filter(Note.note_id == note_id)
            .one_or_none()
    )

    # find it?
    if note is not None:
        note_schema = NoteSchema()
        data = note_schema.dump(note)
        return data

    else:
        abort(404, f'Note not found for ID: {note_id}')


def create(person_id, note):
    """
    creates a new note related to the passed person_id

    :param person_id:
    :param note:
    :return: 201 on success
    """
    # get the person
    person = Person.query.filter(Person.person_id == person_id).one_or_none()

    # person?
    if person is None:
        abort(404, f'Person not found for: {person_id}')

    schema = NoteSchema()
    new_note = schema.load(note, session=db.session)

    # add note to the db
    person.notes.append(new_note)
    db.session.commit()

    # serialize and return the newly created note
    data = schema.dump(new_note)

    return data, 201


def update(person_id, note_id, note):
    """
    update an existing note related to the passed in person_id

    :param person_id:
    :param note_id:
    :param note:
    :return: 200 on success
    """
    update_note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # find a note?
    if update_note is not None:
        # turn note into a db object
        schema = NoteSchema()
        update = schema.load(note, session=db.session)

        # set the IDs to the note we want to update
        update.person_id = update_note.person_id
        update.note_id = update_note.note_id

        # merge the new object, commit to db
        db.session.merge(update)
        db.session.commit()

        # return updated note
        data = schema.dump(update_note)

        return data, 200

    else:
        abort(404, f'Note not found for ID: {note_id}')


def delete(person_id, note_id):
    """
    delete a note from notes structure

    :param person_id:
    :param note_id:
    :return: 200 on success, 404 if not found
    """
    # get the note
    note = (
        Note.query.filter(Person.person_id == person_id)
        .filter(Note.note_id == note_id)
        .one_or_none()
    )

    # note?
    if note is not None:
        db.session.delete(note)
        db.session.commit()
        return make_response(
            f"Note {note_id} deleted.", 200
        )

    else:
        abort(404, f'Note not found for ID: {note_id}')


# -*- coding: utf-8 -*-
from model.person import Person
from  random import randrange
import random


def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.add_contact_fill_form(Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))

    old_contacts = db.get_contact_list()

    index = old_contacts.index(random.choice(old_contacts))
    contact = Person(firstname="UU", lastname="UU", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index,contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        def clean(contact):
            return Person(id=contact.id,firstname=contact.firstname.strip(),lastname=contact.lastname.strip())
        new_contacts = map(clean,db.get_contact_list())
        assert sorted(new_contacts, key = Person.id_or_max) == sorted(app.contact.get_contact_list(), key = Person.id_or_max)

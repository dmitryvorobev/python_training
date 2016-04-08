# -*- coding: utf-8 -*-
from model.person import Person
from  random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact_fill_form(Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Person(firstname="UU", lastname="UU", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index,contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]=contact
    assert sorted(old_contacts, key = Person.id_or_max) == sorted(new_contacts,key = Person.id_or_max)

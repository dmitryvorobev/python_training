# -*- coding: utf-8 -*-
from model.person import Person


def test_add_contact(app):
    contact = Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980")
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact_fill_form(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts,key = Person.id_or_max) == sorted(new_contacts,key = Person.id_or_max)



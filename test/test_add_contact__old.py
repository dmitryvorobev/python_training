# -*- coding: utf-8 -*-
from model.person import Person
import pytest
import random
import string

def test_add_contact(app):
    contact = Person(firstname=app.session.get_random_string(), lastname=app.session.get_random_string(), company=app.session.get_random_string(),
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980")
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact_fill_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts,key = Person.id_or_max) == sorted(new_contacts,key = Person.id_or_max)

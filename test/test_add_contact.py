# -*- coding: utf-8 -*-
from model.person import Person
import pytest
import random
import string


def test_add_contact(app, json_contacts, check_ui,db):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_contact_fill_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    if check_ui:
        def clean(contact):
            return Person(id=contact.id,firstname=contact.firstname.strip(),lastname=contact.lastname.strip())
        old_contacts.append(contact)
        new_contacts = map(clean,db.get_contact_list())
        assert sorted(new_contacts, key = Person.id_or_max) == sorted(app.contact.get_contact_list(), key = Person.id_or_max)


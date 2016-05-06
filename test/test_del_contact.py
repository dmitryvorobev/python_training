# -*- coding: utf-8 -*-
from model.person import Person
from  random import randrange
import random



def test_delete_contact(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_fill_form(Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    if check_ui:
        def clean(contact):
            return Person(id=contact.id,firstname=contact.firstname.strip(),lastname=contact.lastname.strip())
        old_contacts.remove(contact)
        new_contacts = map(clean,db.get_contact_list())
        assert sorted(new_contacts, key = Person.id_or_max) == sorted(app.contact.get_contact_list(), key = Person.id_or_max)


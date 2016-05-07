# -*- coding: utf-8 -*-
from model.person import Person
from model.group import Group
from  random import randrange
import random



def test_add_contact_to_group(app,db,check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_contact_fill_form(Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)

    old_groups = db.get_group_list()
    group = random.choice(old_groups)

    app.contact.add_contact_to_group_by_id(contact.id,group.name)
    l=len(app.contact.get_contact_list_by_group(group))

    assert len(old_contacts) - 1 == app.contact.count()
    if check_ui:
        def clean(contact):
            return Person(id=contact.id,firstname=contact.firstname.strip(),lastname=contact.lastname.strip())
        old_contacts.remove(contact)
        new_contacts = map(clean,db.get_contact_list())
        assert sorted(new_contacts, key = Person.id_or_max) == sorted(app.contact.get_contact_list(), key = Person.id_or_max)


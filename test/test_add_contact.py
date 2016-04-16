# -*- coding: utf-8 -*-
from model.person import Person
import pytest
import random
import string

def random_string(prefix,maxlen):
    symbol = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


test_data = [Person(firstname="", lastname="", company="", address="",home_phone_num="",year="")] + [
    Person(firstname=random_string("firstname",10), lastname=random_string("lastname",20), company=random_string("company",20),
           address=random_string("address",40),home_phone_num=random_string("home_phone_num",20),year=random_string("",5))
    for i in range(5)
    ]

@pytest.mark.parametrize("contact",test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact_fill_form(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts,key = Person.id_or_max) == sorted(new_contacts,key = Person.id_or_max)


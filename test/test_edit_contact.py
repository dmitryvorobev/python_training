# -*- coding: utf-8 -*-
from model.person import Person


def test_add_contact(app):

    app.contact.edit_contact(Person(firstname="UU", lastname="UU", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))


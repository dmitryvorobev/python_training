# -*- coding: utf-8 -*-
from model.person import Person



def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact_fill_form(Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))
    app.contact.delete_first_contact()


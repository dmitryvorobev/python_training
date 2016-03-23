# -*- coding: utf-8 -*-
from model.person import Person


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_contact_fill_form(Person(firstname="John", lastname="Doe", company="paramount",
                                             address="23168 CA, sunbeach blvd", home_phone_num="555111000", year="1980"))
    app.session.logout()


# -*- coding: utf-8 -*-
from model.person import Person


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()


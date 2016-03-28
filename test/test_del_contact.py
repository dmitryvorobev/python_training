# -*- coding: utf-8 -*-
from model.person import Person


def test_add_contact(app):
    app.contact.delete_first_contact()


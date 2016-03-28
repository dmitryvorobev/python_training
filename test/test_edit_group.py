
from model.group import Group


def test_rename_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited", header="edited", footer="edited"))
    app.session.logout()


def test_rename_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="new"))
    app.session.logout()
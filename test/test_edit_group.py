
from model.group import Group


def test_rename_first_group(app):
    app.group.edit_first_group(Group(name="edited", header="edited", footer="edited"))


def test_rename_first_group_name(app):
    app.group.edit_first_group(Group(name="new"))

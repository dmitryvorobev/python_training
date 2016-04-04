
from model.group import Group


def test_rename_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="edited", header="edited", footer="edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_rename_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first_group(Group(name="new"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

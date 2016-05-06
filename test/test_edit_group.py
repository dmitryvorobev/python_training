
from model.group import Group
from  random import randrange
import random


def test_rename_first_group(app,db,check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    chosen_group = random.choice(old_groups)
    index = old_groups.index(chosen_group)
    group = Group(name="edited1", header="edited", footer="edited")
    group.id=chosen_group.id
    app.group.edit_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index]=group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups,key = Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)

# def test_rename_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(name="new"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

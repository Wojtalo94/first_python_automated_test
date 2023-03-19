from model.group import Group
import random


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_mod = Group(name="NewGroupName")
    app.group.modify_group_by_id(group.id, group_mod)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="test2"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_mod = Group(header="NewGroupHeader")
    app.group.modify_group_by_id(group.id, group_mod)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(footer="test3"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_mod = Group(footer="NewGroupFooter")
    app.group.modify_group_by_id(group.id, group_mod)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

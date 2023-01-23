from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    app.group.modify_first_group(Group(name="NewGroupName"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test2"))
    app.group.modify_first_group(Group(header="GroupModified"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test3"))
    app.group.modify_first_group(Group(footer="GroupModified"))


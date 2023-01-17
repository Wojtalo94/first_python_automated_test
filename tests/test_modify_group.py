from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="ToModifyGroup", header="ToModifyGroup", footer="ToModifyGroup"))
    app.group.modify_group(Group(name="GroupModified", header="GroupModified", footer="GroupModified"))
    app.session.logout()

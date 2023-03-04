from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# tutaj sprawdzić jeszcze, ale najprawdopodobniej wszystko jest ok
def test_add_some_contact_to_some_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Jan", middlename="Marek", lastname="Kowalski", nickname="Kowal",
                                   title="mgr", company="IT", address="Cracow 33-800", home_phone="111222333",
                                   mobile_phone="444555666", work_phone="777888999", fax="123456789",
                                   email="test1@gmail.com", email2="test2@gmail.com", email3="test3@gmail.com",
                                   homepage="www.test.com", bday="13", bmonth="June", byear="1992", aday="10",
                                   amonth="April", ayear="2013", address2="Test1", phone2="987654321", notes="Test3"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))

    old_contacts = db.get_contact_list()
    group_list = db.get_contact_list()
    contact = random.choice(old_contacts)
    group = random.choice(group_list)
    start_list = orm.get_contacts_in_group(group.id)
    app.contact.add_contact_to_group_by_id(contact.id, group.name)
    check_list = orm.get_contacts_in_group(group.id)

    assert len(start_list) + 1 == len(check_list)
    start_list.append(contact)
    assert start_list == check_list


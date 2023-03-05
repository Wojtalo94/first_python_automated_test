from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db):
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
        contact = random.choice(old_contacts)
        app.contact.add_contact_to_group_by_id(contact.id)
        # poniższy warunek mi nie działa, a fajnie by było sprawdzić czy jest coś w tabeli w kontakty w grupach
    if len(db.get_group_list_with_added_contacts()) == 0:
        contact_list = orm.get_contact_list()
        contact = random.choice(contact_list)
        group_list = orm.get_group_list()
        group = random.choice(group_list)
        app.contact.add_contact_to_group_by_id(contact.id, group.id)

    groups_with_contacts = db.get_group_list_with_added_contacts()
    group1 = random.choice(groups_with_contacts)
    # start_list = orm.get_contacts_not_in_group(group1)

    before_list = orm.get_contacts_in_group(group1)
    contact = random.choice(before_list)




    # gościu poniżej usuwa kontakt z grupy za pomocą bazy danych zamiast UI. Według mnie trzeba pobrać z bazy danych ID
    # gdzie jest kontakt w grupie, i za pomocą tego id wybrać grupę z listy, usunąć grupę + sprawdzenia
    db.delete_contact_from_group_by_id(contact.id, group1.id)
    after_list = orm.get_contacts_in_group(group1)
    print("\n group1.id = " + group1.id, "\n contact.id = " + contact.id, "\n before_list = " + before_list,
          "\n after_list = " + after_list)






    # check_list = orm.get_contacts_not_in_group(group1)

    # assert len(before_list) - 1 == len(after_list)
    # assert len(start_list) + 1 == len(check_list)
    # before_list.remove(contact)
    # assert sorted(before_list, key=Group.id_or_max) == sorted(after_list, key=Group.id_or_max)

    # old_contacts = db.get_contact_list()
    # contact = random.choice(old_contacts)
    # app.contact.delete_contact_by_id(contact.id)
    # new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    # old_contacts.remove(contact)
    # assert old_contacts == new_contacts
    # if check_ui:
        # assert sorted(new_contacts, key=Group.id_or_max) == sorted(app.contact.get_contact_list(), key=Group.id_or_max)
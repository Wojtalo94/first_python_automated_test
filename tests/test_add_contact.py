# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Jan", middlename="Marek", lastname="Kowalski", nickname="Kowal", title="mgr",
                               company="IT", address="Cracow 33-800", home_phone="111222333", mobile_phone="444555666",
                               work_phone="777888999", fax="123456789", email="test1@gmail.com",
                               email2="test2@gmail.com", email3="test3@gmail.com", homepage="www.test.com", bday="13",
                               bmonth="June", byear="1992", aday="10", amonth="April", ayear="2013", address2="Test1",
                               phone2="987654321", notes="Test3")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="",
                               homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="",
                               phone2="", notes="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

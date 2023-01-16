# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Jan", middlename="Marek", lastname="Kowalski", nickname="Kowal", title="mgr", company="IT", address="Cracow 33-800", home_phone="111222333", mobile_phone="444555666", work_phone="777888999", fax="123456789", email="test1@gmail.com", email2="test2@gmail.com", email3="test3@gmail.com", homepage="www.test.com", bday="13", bmonth="June", byear="1992", aday="10", amonth="April", ayear="2013", address2="Test1", phone2="Test2", notes="Test3"))
    app.contact.return_to_home_page()
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="", phone2="", notes=""))
    app.contact.return_to_home_page()
    app.session.logout()

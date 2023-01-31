from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Jan", middlename="Marek", lastname="Kowalski", nickname="Kowal", title="mgr",
                               company="IT", address="Cracow 33-800", home_phone="111222333", mobile_phone="444555666",
                               work_phone="777888999", fax="123456789", email="test1@gmail.com",
                               email2="test2@gmail.com", email3="test3@gmail.com", homepage="www.test.com", bday="13",
                               bmonth="June", byear="1992", aday="10", amonth="April", ayear="2013", address2="Test1",
                               phone2="987654321", notes="Test3"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

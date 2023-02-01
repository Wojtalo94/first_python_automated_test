from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="NewName")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(middlename="test"))
#    app.contact.modify_first_contact(Contact(middlename="NewMidName"))


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="test"))
#    app.contact.modify_first_contact(Contact(lastname="NewLastName"))


#def test_modify_contact_nickname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(nickname="test"))
#    app.contact.modify_first_contact(Contact(nickname="NewNickname"))


#def test_modify_contact_title(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(title="test"))
#    app.contact.modify_first_contact(Contact(title="NewMgr"))


#def test_modify_contact_company(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(company="test"))
#    app.contact.modify_first_contact(Contact(company="NewIT"))


#def test_modify_contact_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(address="test"))
#    app.contact.modify_first_contact(Contact(address="NewCracow 15"))


#def test_modify_contact_home_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(home_phone="123"))
#    app.contact.modify_first_contact(Contact(home_phone="333222111"))


#def test_modify_contact_mobile_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(mobile_phone="456"))
#    app.contact.modify_first_contact(Contact(mobile_phone="666555444"))


#def test_modify_contact_work_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(work_phone="789"))
#    app.contact.modify_first_contact(Contact(work_phone="999888777"))


#def test_modify_contact_fax(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(fax="987"))
#    app.contact.modify_first_contact(Contact(fax="987654321"))


#def test_modify_contact_email(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(email="test@gmail.com"))
#    app.contact.modify_first_contact(Contact(email="newTest1@gmail.com"))


#def test_modify_contact_second_email(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(email2="test@gmail.com"))
#    app.contact.modify_first_contact(Contact(email2="newTest2@gmail.com"))


#def test_modify_contact_third_email(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(email3="test@gmail.com"))
#    app.contact.modify_first_contact(Contact(email3="newTest3@gmail.com"))


#def test_modify_contact_homepage(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(homepage="www.test.com"))
#    app.contact.modify_first_contact(Contact(homepage="www.newtest.com"))


#def test_modify_contact_birthday_day(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(bday="2"))
#    app.contact.modify_first_contact(Contact(bday="1"))


#def test_modify_contact_birthday_month(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(bmonth="June"))
#    app.contact.modify_first_contact(Contact(bmonth="May"))


#def test_modify_contact_birthday_year(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(byear="2012"))
#    app.contact.modify_first_contact(Contact(byear="2000"))


#def test_modify_contact_anniversary_day(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(aday="2"))
#    app.contact.modify_first_contact(Contact(aday="1"))


#def test_modify_contact_anniversary_month(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(amonth="June"))
#    app.contact.modify_first_contact(Contact(amonth="May"))


#def test_modify_contact_anniversary_year(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="2000"))
#    app.contact.modify_first_contact(Contact(ayear="2012"))


#def test_modify_contact_second_address(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(address2="test"))
#    app.contact.modify_first_contact(Contact(address2="NewTest1"))


#def test_modify_contact_second_phone(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(phone2="987"))
#    app.contact.modify_first_contact(Contact(phone2="123456789"))


#def test_modify_contact_notes(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(notes="test"))
#    app.contact.modify_first_contact(Contact(notes="NewTest3"))

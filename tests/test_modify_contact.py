from model.contact import Contact
from random import randrange


def test_modify_some_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewName")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_middlename(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(middlename="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(middlename="NewMidName")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="NewLastName")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_nickname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(nickname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(nickname="NewNickname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_title(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(title="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(title="NewMgr")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_company(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(company="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(company="NewIT")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(address="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(address="NewCracow 15")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_home_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(home_phone="123"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(home_phone="333222111")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_mobile_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(mobile_phone="456"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(mobile_phone="666555444")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_work_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(work_phone="789"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(work_phone="999888777")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_fax(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fax="987"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(fax="987654321")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_some_contact_email(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(email="test@gmail.com"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(email="newTest1@gmail.com")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_second_email(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(email2="test@gmail.com"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(email2="newTest2@gmail.com")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_third_email(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(email3="test@gmail.com"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(email3="newTest3@gmail.com")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_homepage(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(homepage="www.test.com"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(homepage="www.newtest.com")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_birthday_day(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(bday="2"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(bday="1")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_birthday_month(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(bmonth="June"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(bmonth="May")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_birthday_year(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(byear="2012"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(byear="2000")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_anniversary_day(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(aday="2"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(aday="1")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_anniversary_month(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(amonth="June"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(amonth="May")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_anniversary_year(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(ayear="2000"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(ayear="2012")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_second_address(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(address2="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(address2="NewTest1")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_second_phone(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(phone2="987"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(phone2="123456789")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_notes(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(notes="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(notes="NewTest3")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

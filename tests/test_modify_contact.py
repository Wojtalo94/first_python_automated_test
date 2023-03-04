from model.contact import Contact
import random


def test_modify_all_contact_fields_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_mod = Contact(firstname="edit1", middlename="edit2", lastname="edit3", nickname="edit4", title="edit5",
                          company="edit6", address="edit7", home_phone="111222333", mobile_phone="444555666",
                          work_phone="777888999", fax="0123456789", email="edit8", email2="edit9", email3="edit10",
                          homepage="edit11", bday="18", bmonth="May", byear="1992", aday="13", amonth="June",
                          ayear="2012", address2="edit12", phone2="987654321", notes="edit13")
    app.contact.modify_contact_by_id(contact.id, contact_mod)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_firstname_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(firstname="edit1")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_middlename_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(middlename="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(middlename="NewMidName")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_lastname_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(lastname="NewLastName")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_nickname_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(nickname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(nickname="NewNickname")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_title_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(title="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(title="NewMgr")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_company_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(company="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(company="NewIT")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_address_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(address="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(address="NewCracow 15")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_home_phone_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(home_phone="123"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(home_phone="333222111")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_mobile_phone_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(mobile_phone="456"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(mobile_phone="666555444")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_work_phone_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(work_phone="789"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(work_phone="999888777")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_fax_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(fax="987"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(fax="987654321")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_email_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(email="test@gmail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(email="newTest1@gmail.com")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_second_email_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(email2="test@gmail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(email2="newTest2@gmail.com")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_third_email_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(email3="test@gmail.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(email3="newTest3@gmail.com")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_homepage_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(homepage="www.test.com"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(homepage="www.newtest.com")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_birthday_day_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(bday="2"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(bday="1")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_birthday_month_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(bmonth="June"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(bmonth="May")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_birthday_year_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(byear="2012"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(byear="2000")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_anniversary_day_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(aday="2"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(aday="1")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_anniversary_month_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(amonth="June"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(amonth="May")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_anniversary_year_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(ayear="2000"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(ayear="2012")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_second_address_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(address2="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(address2="NewTest1")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_second_phone_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(phone2="987"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(phone2="123456789")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_modify_contact_notes_by_id(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(notes="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_modify = Contact(notes="NewTest3")
    app.contact.modify_contact_by_id(contact.id, contact_modify)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

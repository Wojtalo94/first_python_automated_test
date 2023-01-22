from model.contact import Contact


def test_modify_contact(app):
    app.contact.create(Contact(firstname="Jan", middlename="Marek", lastname="Kowalski", nickname="Kowal", title="mgr",
                               company="IT", address="Cracow 33-800", home_phone="111222333", mobile_phone="444555666",
                               work_phone="777888999", fax="123456789", email="test1@gmail.com",
                               email2="test2@gmail.com", email3="test3@gmail.com", homepage="www.test.com", bday="13",
                               bmonth="June", byear="1992", aday="10", amonth="April", ayear="2013", address2="Test1",
                               phone2="987654321", notes="Test3"))
    app.contact.modify_first_contact(Contact(firstname="NewName", middlename="NewMidName", lastname="NewLastName",
                                             nickname="NewNickname", title="NewMgr", company="NewIT", address="NewCracow 15",
                                             home_phone="333222111", mobile_phone="666555444", work_phone="999888777",
                                             fax="987654321", email="newTest1@gmail.com", email2="newTest2@gmail.com",
                                             email3="newTest3@gmail.com", homepage="www.newtest.com", bday="1", bmonth="May",
                                             byear="2000", aday="1", amonth="May", ayear="2012", address2="NewTest1",
                                             phone2="123456789", notes="NewTest3"))

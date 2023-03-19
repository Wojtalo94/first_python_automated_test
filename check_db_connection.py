from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # l = db.get_contacts_in_group(Group(id="234"))
    # l = db.get_contact_list()
    l = db.get_contacts_not_in_group(Group(id="234"))

    for item in l:
        print(item)
    print(len(l))
finally:
    pass  # db.destroy() // tutaj pomijamy dodając zaślepkę, dlatego że ORM automatycznie zamyka połączenie

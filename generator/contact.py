from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import re

# możemy uruchomić cały ten plik aby utworzyć sobie nowe dane dla kontaktu
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "test_data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def clear(s):
    return re.sub("[() -]", "", s)


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join(map(lambda x: clear(x), [random.choice(symbols) for i in range(random.randrange(maxlen))]))


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_phone="", mobile_phone="", work_phone="", fax="", email="", email2="", email3="", homepage="",
                    bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", address2="", phone2="", notes="")] + [
        Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                title=random_string("title", 10), company=random_string("company", 10),
                address=random_string("address", 10), home_phone=str(random.randrange(000000000, 999999999)),
                mobile_phone=str(random.randrange(000000000, 999999999)), work_phone=str(random.randrange(000000000, 999999999)),
                fax=str(random.randrange(0, 999999999999)), email=random_string("email", 15), email2=random_string("email2", 20),
                email3=random_string("email3", 20), homepage=random_string("homepage", 20),
                bday=str(random.randrange(1, 32)), bmonth=random.choice(months), byear=str(random.randrange(1, 2050)),
                aday=str(random.randrange(1, 32)), amonth=random.choice(months), ayear=str(random.randrange(1, 2050)),
                address2=random_string("address2", 30), phone2=str(random.randrange(000000000, 999999999)),
                notes=random_string("notes", 30))
        for i in range(n)
    ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

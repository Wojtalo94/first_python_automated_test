from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact_details(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_date_value("bday", contact.bday)
        self.change_date_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_date_value("aday", contact.aday)
        self.change_date_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def clear_contact_details(self):
        wd = self.app.wd
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("notes").clear()

    def create(self, contact):
        wd = self.app.wd
        self.open_main_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        self.fill_contact_details(contact)
        # submit contact creation
        wd.find_element_by_css_selector('input[name="submit"]').click()
        self.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_to_modify_by_index(index)
        # update contact
        self.fill_contact_details(contact)
        # submit contact modify
        wd.find_element_by_css_selector('input[name="update"]').click()
        self.return_to_home_page()
        self.contact_cache = None

    def select_contact_to_modify_by_index(self, index):
        wd = self.app.wd
        # Edit random contact
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_index(index)
        # click submit delete button
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # click delete button
        wd.find_element_by_css_selector('input[value="Delete"]').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_main_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_main_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last = cells[1].text
                first = cells[2].text
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=last, firstname=first, id=id))
        return list(self.contact_cache)

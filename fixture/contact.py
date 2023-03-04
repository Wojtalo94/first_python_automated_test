from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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

    def modify_contact_by_id(self, id, contact):
        wd = self.app.wd
        # Open page with contacts
        self.open_main_page()
        self.select_contact_by_id(id)
        # edit
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % id).click()
        self.fill_contact_details(contact)
        # update and return
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def select_contact_to_modify_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        # Edit random contact
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_index_to_delete(index)
        # click submit delete button
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_id_to_delete(id)
        # click submit delete button
        wd.switch_to.alert.accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None

    def select_contact_by_index_to_delete(self, index):
        wd = self.app.wd
        # select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        # click delete button
        wd.find_element_by_css_selector('input[value="Delete"]').click()

    def select_contact_by_id_to_delete(self, id):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()
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
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def select_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_main_page()
        # select created contact do view details
        wd.find_elements_by_css_selector('img[alt="Details"]')[index].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.select_contact_to_modify_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, phone2=phone2, email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.select_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)

    def add_contact_to_group_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        self.select_contact_by_id(id)
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath("//div[4]/select/option").click()
        # click Add to (group) button
        wd.find_element_by_name("add").click()
        self.contact_cache = None

    def delete_contact_to_group_by_id(self, id):
        wd = self.app.wd
        self.open_main_page()
        # select third option
        wd.find_element_by_name("group").click()
        wd.find_element_by_xpath("//option[3]").click()
        self.select_contact_by_id(id)
        # click Remove from "{group}" button
        wd.find_element_by_name("remove").click()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

# -*- coding: utf-8 -*-
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
import unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        # open home pag
        wd.get("http://localhost/addressbook/")
        # login
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact firm
        wd.find_element_by_name("firstname").send_keys("Jan")
        wd.find_element_by_name("middlename").send_keys("Marek")
        wd.find_element_by_name("lastname").send_keys("Kowalski")
        wd.find_element_by_name("nickname").send_keys("Kowal")
        wd.find_element_by_name("title").send_keys("mgr")
        wd.find_element_by_name("company").send_keys("IT")
        wd.find_element_by_name("address").send_keys("Cracow 33-800")
        wd.find_element_by_name("home").send_keys("111222333")
        wd.find_element_by_name("mobile").send_keys("444555666")
        wd.find_element_by_name("work").send_keys("777888999")
        wd.find_element_by_name("fax").send_keys("123456789")
        wd.find_element_by_name("email").send_keys("test1@gmail.com")
        wd.find_element_by_name("email2").send_keys("test2@gmail.com")
        wd.find_element_by_name("email3").send_keys("test3@gmail.com")
        wd.find_element_by_name("homepage").send_keys("www.test.com")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("13")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("June")
        wd.find_element_by_xpath("//option[@value='June']").click()
        wd.find_element_by_name("byear").send_keys("1992")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("10")
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[12]").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[5]").click()
        wd.find_element_by_name("ayear").send_keys("2013")
        wd.find_element_by_name("address2").send_keys("Test1")
        wd.find_element_by_name("phone2").send_keys("Test2")
        wd.find_element_by_name("notes").send_keys("Test3")
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to home page
        wd.find_element_by_link_text("home").click()
        # logout
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

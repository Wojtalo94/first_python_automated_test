class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def fill_group_details(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def clear_group_details(self):
        wd = self.app.wd
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_footer").clear()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group firm
        self.fill_group_details(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # find first group to update and click Edit group button
        wd.find_element_by_xpath("//div[@id='content']/form/span/input").click()
        wd.find_element_by_name("edit").click()
        # clear group from details
        self.clear_group_details()
        # fill group firm
        self.fill_group_details(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

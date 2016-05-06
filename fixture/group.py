from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new"))>0):
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_group_by_id(self,id):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_id(id)
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_group_by_index(self,index):
        wd = self.app.wd
        self.open_groups_page()
        # select first group
        self.select_group_by_index(index)
        # delete group
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cash = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        # edit group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cash = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        # edit group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cash = None


    def edit_first_group(self, group):
        self.edit_group_by_index(self, 0, group)

    def fill_group_form(self, group_data):
        wd = self.app.wd
        self.change_field("group_name", group_data.name)
        self.change_field("group_header", group_data.header)
        self.change_field("group_footer", group_data.footer)

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self,index):
        # select first group
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_group_by_id(self,id):
        # select first group
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cash = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cash.append(Group(name=text,id=id))
        return list(self.group_cash)


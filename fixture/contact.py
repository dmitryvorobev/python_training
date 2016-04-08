from model.person import Person

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact_fill_form(self, Person):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Person)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cash = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_xpath("//tr[2]/td/input[@name='selected[]']").click()
        wd.find_element_by_xpath("//div/input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def edit_contact(self, Person):
        wd = self.app.wd
        self.open_contacts_page()
        #select first
        wd.find_element_by_xpath("//tr[2]/td/input[@name='selected[]']").click()
        #click edit by first
        wd.find_element_by_xpath("//tr[2]/td/a/img[@title='Edit']").click()
        self.fill_contact_form(Person)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_xpath("//form/input[@value='Update'][1]").click()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_xpath("//td/input[@name='selected[]']"))

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, Person):
        wd = self.app.wd
        self.change_field("firstname",Person.firstname)
        self.change_field("lastname",Person.lastname)
        self.change_field("company",Person.company)
        self.change_field("address",Person.address)
        self.change_field("home",Person.home_phone_num)
        self.change_field("byear",Person.year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[3]").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("addressbook/")):
            wd.find_element_by_link_text("home").click()

    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tbody/tr[@name='entry']"):
                name = element.find_element_by_xpath("./td[3]").text
                surname = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_xpath("./td/input").get_attribute("id")
                self.contact_cash.append(Person(firstname=name,lastname=surname, id=id))
        return list(self.contact_cash)


from model.person import Person
import random
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact_fill_form(self, Person):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(Person)
        self.push_submit_button()
        self.contact_cash = None

    def push_submit_button(self):
        wd = self.app.wd
        try:
            wd.find_element_by_xpath("//input[@name='submit'][1]").click()
        except:
            wd.find_element_by_xpath("//input[@value='Update'][1]").click()

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div/input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cash = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def edit_contact_by_index(self, index, Person):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(Person)
        self.push_submit_button()
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
        if Person.firstname != "":
            day_list = []
            for element in wd.find_elements_by_xpath("//select[@name='bday']/option"):
                day_list.append(element.text)
            day=random.randrange(2,len(day_list)-2)
            wd.find_elements_by_xpath("//select[@name='bday']/option")[day].click()
            month_list = []
            for element in wd.find_elements_by_xpath("//select[@name='bmonth']/option"):
                month_list.append(element.text)
            month=random.randrange(2,len(month_list)-2)
            wd.find_elements_by_xpath("//select[@name='bmonth']/option")[month].click()


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
                all_phones = element.find_element_by_xpath("./td[6]").text
                if len(all_phones)>1:
                    self.contact_cash.append(Person(firstname=name,lastname=surname, id=id,
                                                    all_phones_from_home_page=all_phones))
                else:
                    self.contact_cash.append(Person(firstname=name,lastname=surname, id=id))
        return list(self.contact_cash)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone_num = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone_num = wd.find_element_by_name("mobile").get_attribute("value")
        workphone_num = wd.find_element_by_name("work").get_attribute("value")
        secondary_num = wd.find_element_by_name("phone2").get_attribute("value")
        return Person(firstname=firstname,lastname=lastname,home_phone_num=home_phone_num,mobile_phone_num=mobile_phone_num,
                      workphone_num=workphone_num,secondary_num=secondary_num,id=id)


    def get_contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone_num = re.search("H: (.*)",text).group(1)
        mobile_phone_num = re.search("M: (.*)",text).group(1)
        workphone_num = re.search("W: (.*)",text).group(1)
        secondary_num = re.search("P: (.*)",text).group(1)
        return Person(home_phone_num=home_phone_num,mobile_phone_num=mobile_phone_num,
                      workphone_num=workphone_num,secondary_num=secondary_num)


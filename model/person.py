from sys import maxsize
class Person:
    def __init__(self, firstname=None, lastname=None, company= None, address= None, home_phone_num= None, mobile_phone_num =None,
                 workphone_num = None, secondary_num = None, year= None, id= None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home_phone_num = home_phone_num
        self.mobile_phone_num = mobile_phone_num
        self.workphone_num = workphone_num
        self.secondary_num = secondary_num
        self.year = year
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page



    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
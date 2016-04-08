from sys import maxsize
class Person:
    def __init__(self, firstname, lastname, company= None, address= None, home_phone_num= None, year= None, id= None):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home_phone_num = home_phone_num
        self.year = year
        self.id = id


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
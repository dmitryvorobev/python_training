import mysql.connector
from model.group import Group
from model.person import Person

class DbFixture:


    def __init__(self, host, name,user,password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password

        self.connection = mysql.connector.connect(host=host, db=name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id,name,header,footer) = row
                list.append(Group(id=str(id),name=name,header=header,footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname FROM addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id,firstname,lastname) = row
                list.append(Person(id=str(id),firstname=firstname,lastname=lastname))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()

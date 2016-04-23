from model.group import Group
from model.person import Person

import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

"""or in command line"""
"""-n 10 -f data/groups.json"""

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a


def random_string(prefix,maxlen):
    symbol = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbol) for i in range(random.randrange(maxlen))])


test_data = [Person(firstname="", lastname="", company="", address="",home_phone_num="",year="")] + [
    Person(firstname=random_string("firstname",10), lastname=random_string("lastname",20), company=random_string("company",20),
           address=random_string("address",40),home_phone_num=random_string("home_phone_num",20),year=random_string("",5))
    for i in range(n)
    ]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",f)

# with open(file,"w") as out:
#     out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent =2)
    out.write(jsonpickle.encode(test_data))
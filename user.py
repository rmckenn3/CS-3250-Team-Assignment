"""
Stores information about customers.
"""
#imports

#People class
class User:
    #initialize variables
    def __init__(self, name, birthday, ssn, address, email=None, phone=None):
        self.name = name
        self.birthday = birthday
        self.ssn = ssn
        self.address = address
        self.phone = phone
        self.email = email
    #end __init__

#end People class
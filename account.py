"""
Manages account information.
"""
#imports

#Account class
class Account:
    #initialize variables
    def __init__(self, holders, type, number, balance):
        self.holders = holders
        self.type = type
        self.number = number
        self.balance = balance
    #end __init__
    
#end Account class
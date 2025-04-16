"""
Manages account information.
"""
#imports

#Account class
class Account:
    #initialize variables
    def __init__(self, primary_holder, account_type, account_number, balance=0, secondary_holders=None, card=None):
        self.primary_holder = primary_holder
        self.account_type = account_type
        self.account_number = account_number
        self.balance = balance
        self.secondary_holders = secondary_holders
        self.card = card
    #end __init__
    
#end Account class
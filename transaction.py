"""
Transaction class contains methods to handle purchases and transfers.
"""
#imports
from datetime import datetime
#Transaction class
class Transaction:
    #initialize variables
    def __init__(self, merchant, amount, card):
        self.merchant = merchant
        self.amount = amount
        self.card = card
        self.date = datetime.now().date()
    #end __init__

#end Transaction class
"""
Transaction class contains methods to handle purchases and transfers.
"""
#imports
from datetime import datetime
#Transaction class
class Transaction:
    #initialize variables
    def __init__(self, source, destination, amount):
        self.source = source
        self.destination = destination
        self.amount = amount
        self.date = datetime.now().date()
    #end __init__

#end Transaction class
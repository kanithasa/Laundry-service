
from demo import *
class CustomerMenu():

    def __init__(self,customer):
        self.customer=customer
        
    def CustomerDetails(self):
        k=self.customer.getDetail()

    def PlaceOrder(self):
        pass

    def Packages(self):
        self.customer.showpackages()   #Displays the packages with their details
        k=self.customer.package        #Stores the customer's package
        #Rest is to link tkinter button with the Customer's package.
        
    def Status(self):
        #Displays the status of the customer's order
        pass

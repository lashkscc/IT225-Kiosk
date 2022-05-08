class Customer():
    def __init__(self, ID, phone):
        self.custID = ID
        self.custPhone=phone

    def setCustPhone(self, phone):
        self.custPhone=phone
    
    def getCustPhone(self):
        return self.custPhone

    def getCustID(self):
        return self.custID

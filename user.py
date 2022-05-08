class User():
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
    
    def setFirstName(self, name):
        self.firstName = name
        
    def setLastName(self, name):
        self.lastName = name

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName
    
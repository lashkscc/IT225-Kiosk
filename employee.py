class Employee():
    def __init__(self, ID, PW):
        self.ID=ID
        self.PW=PW

    def setEmplPW(self, PW):
        self.PW=PW
    def getEmplID(self):
        return self.ID
    def getEmplPW(self):
        return self.PW

        
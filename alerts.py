class Alert():
    def __init__(self, name, details):
        self.tag = name
        self.details = details
        self.alertItems = []
         
    def getAlertTag(self):
        return self.tag
    
    def getAlertDetails(self):
        return self.details

    def addAlertItem(self, item):
        self.alertItems.append(item)
    
    def isItemTagged(self, item):
        if item in self.alertItems:
            return True
        else:
            return False



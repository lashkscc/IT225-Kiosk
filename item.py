class Item():
    def __init__(self, barcodeID, name, expWeight, pricePerUnit, *alertTags): #alertTags will be list of strings
        self.barcode = barcodeID
        self.name = name
        self.weight = expWeight
        self.ppu = pricePerUnit
        self.alerts = [*alertTags]
  
    def getName(self):
        return self.name

    def getPricePerUnit(self):
        return self.ppu
    
    #instead of having a product type, we make reuse expWeight such that if expWeight !=0
    #the product is priced per pound. If expWeight > 0, product is priced per item
    def isPricedByWeight(self):
        if self.weight == 0:
            return True
        else:
            return False
    
    def getAlerts(self):
        return self.alerts

    def addAlert(self, alertTag):
        self.alerts.append(alertTag)
    
    def removeAlert(self, alertTag):
        self.alerts.remove(alertTag)

    def __str__(self):
        return (str(self.barcode) + ' ' + self.name + ' ' + str(self.isPricedByWeight()) + ' ' + str(self.ppu) + ' ' + str(' '.join(self.alerts)))
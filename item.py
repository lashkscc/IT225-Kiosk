#Note, if expWeight = 0, that means the item's price is per weight. If the expect weight exists, that means the item is per quantity



class Item():
    def __init__(self, barcodeID, expWeight, pricePerUnit, *AlertTags):
        self.barcode = barcodeID
        self.weight = expWeight
        self.ppu = pricePerUnit
        self.alerts = AlertTags

    def getPricePerUnit(self):
        return self.ppu
    
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


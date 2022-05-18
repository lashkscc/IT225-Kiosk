class Kiosk():
    def __init__(self, ID):
        self.kioskID = ID
        self.currentCustomer = 0;
        self.scan = 0;
        self.scale = 0;
        self.lock = False;

    def getKioskID(self):
        return self.kioskID
        
    def scanBarcode(self):
        #would be an interface for barcode scanning software
        self.scan = int(input("Barcode:"))
        return self.scan
    
    def getWeight(self):
        #would be an interface for the kiosk's scale
        self.weight= float(input("Weight:"))
        return self.weight

    def lockStatus(self):
        return self.lock

    def setLock(self, status):
        self.lock = status

    def resetKiosk(self):
        self.currentCustomer = 0;
        self.scan = 0;
        self.scale = 0;
        self.lock = False;                

    def __str__(self):
        return (self.kioskID + ' ' + self.currentCustomer + ' ' + self.lock)
    
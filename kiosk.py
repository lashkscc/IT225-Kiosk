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

    def lockKiosk(self):
        self.lock = True

    def unlockKiosk(self):
        self.lock=False

    
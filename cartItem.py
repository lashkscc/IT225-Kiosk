from item import Item
class CartItem():
    def __init__(self, item, weight, *quant): #quant exists only if the item is not priced per pound
        self.item = item
        self.weight = weight
        if len(self.quant)==1:
            self.quantity = quant[0]
     
    def getItem(self):
        return self.item

    def getWeight(self):
        return self.weight
    
    def getQuantity(self):
        return self.quantity
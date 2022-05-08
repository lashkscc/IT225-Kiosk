from cartItem import CartItem


class ShoppingCart():
    def __init__(self):
        self.cartItems=[]
    
    def addItem(self,cartItem):
        self.cartItems.append(cartItem)
    
    def removeItem(self, cartItem):
        self.cartItems.remove(cartItem)
 
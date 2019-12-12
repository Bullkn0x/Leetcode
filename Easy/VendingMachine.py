'''
Create a Vending machine that will take money and store items
'''
class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def updateStock(self, stock):
        self.stock = stock

    def buyFromStock(self):
        if self.stock == 0:
            return 'item out of stock'

        else: 
            self.stock -=1

class VendingMachine:
    def __init__(self):
        self.bank = 0
        self.items = []
        self.headers = ['Item','Price','Qty']
        

    def addItem(self, item):
        self.items.append(item)

    def showItems(self):
        dash = '-' * 33
        headfmt='{:<10s}{:>10s}{:>11s}'
        tablefmt='{:<10s}{:>8d}{:>12d}'
        print(dash)
        print(headfmt.format(self.headers[0], self.headers[1],self.headers[2]))
        print(dash)
        for item in self.items:
            print(tablefmt.format(item.name, item.price, item.stock))

    def addCash(self, money):
        self.bank += money
    
    def getItem(self, itemWanted):
        for item in self.items:
            if item.name == itemWanted:
                return item 
        return None 
        

    
    def showCash(self):
        print(f'Currently you have: {self.bank} tokens')

    def buyItem(self , itemWanted):
        found=False
        for item in self.items:
            if item.name == itemWanted:
                found=True
                break
            print('Item Not available')

        if found:
            if self.bank >= item.price:
                self.bank -= item.price
                item.buyFromStock()
                print('You got ' +item.name)
                print('Cash remaining: ' + str(self.bank))
            else:
                print(f'Sorry Dingleberry you need {int(item.price-self.bank)} more coins to purchase this thing you poor chingus')

class User:

    def __init__(self, firstName):
        self.firstName= firstName
        self.purchaseHistory=[]
        


newvending=VendingMachine()
item1 = Item('Vegan Eggs' , 10, 1)
newvending.addItem(item1)
item1 = Item('Cheese' , 10, 4)
newvending.addItem(item1)
item1 = Item('Milk' , 10, 4)
newvending.addItem(item1)

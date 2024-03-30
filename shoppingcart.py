class ItemToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    
    
    def __init__(self,item_name, item_price,item_quantity):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def __init__(self,item_name, item_price,item_quantity, item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description


    def print_item_cost (self):
        print(self.item_name," ", self.item_quantity, " @ ", self.item_price)
        return self.item_quantity*self.item_price
    

class ShoppingCart:
    def _init_(self):
        self.self.customer_name = 'none'
        self.date = 'January 1 2020'
        
        
    def __init__(self, customer_name, date,cart_items):
        self.customer_name = customer_name
        self.date = date
        self.cart_items = cart_items
        
    
    
    def add_item(self,ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    
    def remove_item(self,ItemToReturn):
        if(ItemToReturn in self.cart_items[:]):
            self.cart_items.remove(ItemToReturn)
        else:
            print(' Item not found in cart. Nothing removed.')
            
    def modify_item(self,ItemToPurchase):
        try:
            i = self.cart_items.index(ItemToPurchase)
            #self.cart_items[i][1] = input('Enter modified description')
            #self.cart_items[i][2] = int(input('Enter modified price'))
            self.cart_items[i][3] = int(input('Enter modified quantity'))
        except ValueError:
               print( 'Item not found in cart. Nothing modified.')
    
    
    def get_num_items_in_cart(self):
      return len(cart_items)
    
    def get_cost_of_cart(self):
        cost = 0
        index = 0
        while (index<len(self.cart_items)):
          cost = cost + self.cart_items[index][2]*self.cart_items[index][3]
          index = index + 1
        return cost

    def print_total(self):
        try:
            i = 0
            print ('OUTPUT SHOPPING CART')
            print(self.customer_name, '-', self.date)
            while (i<len(self.cart_items)):
                total = self.cart_items[i][2]*self.cart_items[i][3]
                print (self.cart_items[i][0], self.cart_items[i][2], ' @ ', self.cart_items[i][1], ' = ', total)
                i = i + 1
        except ValueError:
            print ('SHOPPING CART IS EMPTY')
    
    def print_descriptions(self):
        try:
            i = 0
            print ('OUTPUT ITEMS\' DESCRIPTIONS')
            print(self.customer_name, '-', self.date)
            while (i<len(self.cart_items)):
                print(self.cart_items[i][0],' : ', self.cart_items[i][1])
                i = i + 1
        except ValueError:
            print ('SHOPPING CART IS EMPTY')
        
         
item1name = str(input('Enter item 1 name'))
item1price = float(input('Enter item 1 price'))
item1quantity = int(input('Enter item 1 quantity'))
item_to_purchase_1 = ItemToPurchase (item1name,item1price,item1quantity,'')

item2name = str(input('Enter item 2 name'))
item2price = float(input('Enter item 2 price'))
item2quantity = int(input('Enter item 2 quantity'))
item_to_purchase_2 = ItemToPurchase (item2name, item2price, item2quantity,'')

print ('TOTAL COST')
cost1 = item_to_purchase_1.print_item_cost()
cost2 = item_to_purchase_2.print_item_cost()
totalcost = cost1 + cost2
print ('Total: ', totalcost)

    
        
              

entercustomername = str(input('Enter customer name'))
todaysdate = str(input('Enter today\'s date'))
#shoppingcart = ShoppingCart(entercustomername,todaysdate,[item_to_purchase_1,item_to_purchase_2])
shoppingcart = ShoppingCart(entercustomername,todaysdate,[])
print('Customer Name:', entercustomername)
print('Today\'s date:', todaysdate)
command = input('Enter command (a/r/c/i/o/q): ')
while command != 'q':
    if command == 'a': 
        print('ADD ITEM TO CART')
        itemToPurchase_itemname = str(input('enter item name:'))
        itemToPurchase_itemdescription = str(input('enter item description'))
        itemToPurchase_itemquantity = int(input('Enter item quantity:'))
        itemToPurchase_itemprice = float(input('Enter item price'))
        itemToPurchaseNew = ItemToPurchase(itemToPurchase_itemname,itemToPurchase_itemquantity,itemToPurchase_itemprice, itemToPurchase_itemdescription)
        shoppingcart.add_item(itemToPurchaseNew)
    if command == 'r': 
        print('REMOVE ITEM FROM CART')
        itemToReturn = input('Enter item to return')
        shoppingcart.add_item(itemToReturn)
    if command == 'c': 
        print('CHANGE ITEM QUANTITY')
        changeItem = [x for x in input("Enter item to change: ").split()]
        itemTochange_itemname = ItemToPurchase(changeItem,0,0,'')
        shoppingcart.modify_item(changeItem)
    if command == 'i':
        shoppingcart.print_descriptions()
    if command == 'o':
        shoppingcart.print_total()
    command = input('Enter command (a/r/c/i/o/q): ')

        
         



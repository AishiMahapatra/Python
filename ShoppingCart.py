class ItemToPurchase:
     def _init_(self):
      self.item_name = 'none'
      self.item_price = 0.0
      self.item_quantity = 0
     
     def print_item_cost(self):
      print(self.item_name,' ', self.item_quantity, ' @ ', self.item_price, '\n')
    
    
item1 = ItemToPurchase()
item1.item_name ='Chocolate Chip'
item1.item_price = 1
item1.item_quantity = 3
     
item2 = ItemToPurchase()
item2.item_name ='Bottled Water'
item2.item_price = 1
item2.item_quantity = 10
        
print('Total Cost \n')
item1.print_item_cost()
item2.print_item_cost()
print(item1.item_quantity*item1.item_price + item2.item_quantity*item2.item_price)

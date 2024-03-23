from test.support.threading_helper import catch_threading_exception
class ShoppingCart:
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
            self.cart_items[i][1] = input('Enter modified description')
            self.cart_items[i][2] = int(input('Enter modified price'))
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
        
         

    
        
              
shoppingcart = ShoppingCart('John Doe','February 1, 2020',[['Nike Romaleos','Volt color, Weightlifting shoes', 2, 189], ['Chocolate Chips', 'Semi-Sweet',5, 3], ['Powerbeats 2 Headphone', 'Bluetooth Headphone', 1, 128]])
command = input('Enter command (a/r/c/i/o/q): ')
while command != 'q':
    if command == 'a': 
        itemToPurchase = [x for x in input("Enter item to purchase: ").split()]
        shoppingcart.add_item(itemToPurchase)
    if command == 'r': 
        itemToReturn = input('Enter item to return')
        shoppingcart.add_item(itemToReturn)
    if command == 'c': 
        changeItem = [x for x in input("Enter item to purchase: ").split()]
        shoppingcart.modify_item(changeItem)
    if command == 'i':
        shoppingcart.print_descriptions()
    if command == 'o':
        shoppingcart.print_total()
    command = input('Enter command (a/r/c/i/o/q): ')

        
         
        
        
    

    
        
        
       
    
    
  
    
               
            
        
    
    

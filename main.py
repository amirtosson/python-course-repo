"""
@author:    Python Course
@license:   GNU General Public License v3 or higher
@copyright: Universität Siegen, Deutschland
@email:     tosson@physik.uni-siegen.de
"""

"""
summary:    A testing file  
name:       main
date:       30.12.2021
"""




class SellingProduct:
    price = 1.00
    name = "product name"
    buyer = "buyer name"
    storage = 0
    is_order_placed = False


    def __init__(self, product_name, product_price, product_storage, 
                 product_is_ordered):
        self.name = product_name
        self.price = product_price
        self.storage = product_storage
        self.is_order_placed = product_is_ordered
        

    def printing_details(self):
        print("The product name is " + self.name)
        print("The product price is " + str(self.price))
        print("The product buyer is " + self.buyer)
        print("We have  " + str(self.storage) + " items in our store")
        if self.is_order_placed:
            print("There is an order")
        else:
            print("There is no order yet")

    def change_product_price(self, new_price):
        self.price = new_price
        
    def change_product_name(self, new_name):
        self.name = new_name
        
    def change_product_buyer_name(self, new_buyer_name):
        self.buyer = new_buyer_name
    
    def change_product_storage(self, new_storage):
        self.storage = new_storage
        
    def change_product_is_order_placed(self, new_is_order_placed):
        self.is_order_placed = new_is_order_placed






done = False

all_products = [ ]
while done != True:  
    x = input("What do you want to do? \n a to add new product \n c to change a product \n q quite\n")
    
    if x == "a":
        user_product_name = input("Enter the product name ")
        user_product_price = float(input("Enter the product price "))
        user_product_storage = int(input("Enter the product storage "))
        user_product_ordered = input("Any order placed? y for yes and n for no ")
        is_ordered = False 

        if user_product_ordered == "y":
            is_ordered = True
        
        product_1 = SellingProduct(user_product_name, user_product_price
                                   , user_product_storage, is_ordered)
        all_products.append(product_1)

        
    elif x == "c":
        products_we_have = len(all_products)
        
        if products_we_have == 0:
            print("We have no Products, please add products ")
            continue
        
        print("We have " + str(products_we_have) + " Products")
        product_id = int(input("Which one to change? ")) 
        
        if products_we_have < product_id:
            print("Invalid product number ")
            continue
        
        product_to_change = all_products[product_id - 1]
        
        to_change = input("What do you want to change? n for name, p for price, \n b for buyer, s for storage, and o for order ")
        
        if to_change == "n":
            new_name = input("Enter the product name ")
            product_to_change.change_product_name(new_name)
        elif to_change == "p":
            new_price = float(input("Enter the product name "))
            product_to_change.change_product_price(new_price)
        elif to_change == "b":
            new_buyer = input("Enter the buyer name ")
            product_to_change.change_product_buyer(new_buyer)
        elif to_change == "s":
            new_storage = int(input("Enter the storage "))
            product_to_change.change_product_storage(new_storage)
        elif to_change == "o":
            user_product_ordered = input("Any order placed? y for yes and n for no ")
            is_ordered = False 
            if user_product_ordered == "y":
                is_ordered = True  
            product_to_change.change_product_is_order_placed(is_ordered)
            
    elif x == "q":
        break
    else:
        continue
        
    
    



"""
user_product_name = input("Enter the product name ")
user_product_price = float(input("Enter the product price "))
user_product_storage = int(input("Enter the product storage "))
user_product_ordered = input("Any order placed? y for yes and n for no ")
is_ordered = False 

if user_product_ordered == "y":
    is_ordered = True

product_1 = SellingProduct(user_product_name, user_product_price
                           , user_product_storage, is_ordered)

"""
#product_1 = SellingProduct("user_name", 30.66
                           #,100 ,False)

#product_1.printing_details()
#product_1.change_product_name("Our Product")
#product_1.change_product_price(60.30)
#product_1.printing_details()


"""
To add a product 
To change a detail or details
To print all the availble products
To print a specific product
"""


    
    
    
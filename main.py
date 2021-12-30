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



"""
class to define a selling products
variables: price -> is the price of the product
            name -> is the name of the product
            buyer -> is the name of the buyer
            storage
            is_order_placed           
"""
class SellingProduct:
    price = 1.00
    name = "product name"
    buyer = "buyer name"
    storage = 0
    is_order_placed = False

    # name, price, storage, and is_order?place must be intialized
    def __init__(self, product_name, product_price, product_storage, 
                 product_is_ordered):
        self.name = product_name
        self.price = product_price
        self.storage = product_storage
        self.is_order_placed = product_is_ordered
        
    # print everything
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

class BuyingProduct:
    price = 1.00
    name = "product name"
    seller = "seller name"
    delivery_date = "01.01.2000"

    def __init__(self, product_name, product_price, product_seller, 
                 product_delivery_date):
        self.name = product_name
        self.price = product_price
        self.seller = product_seller
        self.delivery_date = product_delivery_date
        

    def printing_details(self):
        print("The product name is " + self.name)
        print("The product price is " + str(self.price))
        print("The product seller is " + self.seller)
        print("The delivery date is " + self.delivery_date)

    def change_product_price(self, new_price):
        self.price = new_price
        
    def change_product_name(self, new_name):
        self.name = new_name
        
    def change_product_seller_name(self, new_seller_name):
        self.seller = new_seller_name
    
    def change_product_delivery_date(self, new_delivery_date):
        self.delivery_date = new_delivery_date
        

done = False

selling_products = [ ]

buying_products = [ ]

while done != True:  
    section = input("Which section? s for selling, b for buying and q to quite. ")
    if section == "s":
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
            selling_products.append(product_1)
              
        elif x == "c":
            products_we_have = len(selling_products)
            
            if products_we_have == 0:
                print("We have no Products, please add products ")
                continue
            
            print("We have " + str(products_we_have) + " Products")
            product_id = int(input("Which one to change? ")) 
            
            if products_we_have < product_id:
                print("Invalid product number ")
                continue
            
            product_to_change = selling_products[product_id - 1]
            
            to_change = input("What do you want to change? n for name, p for price, \n b for buyer, s for storage, and o for order ")
            
            if to_change == "n":
                new_name = input("Enter the product name ")
                product_to_change.change_product_name(new_name)
            elif to_change == "p":
                new_price = float(input("Enter the product name "))
                product_to_change.change_product_price(new_price)
            elif to_change == "b":
                new_buyer = input("Enter the buyer name ")
                product_to_change.change_product_buyer_name(new_buyer)
            elif to_change == "s":
                new_storage = int(input("Enter the storage "))
                product_to_change.change_product_storage(new_storage)
            elif to_change == "o":
                user_product_ordered = input("Any order placed? y for yes and n for no ")
                is_ordered = False 
                if user_product_ordered == "y":
                    is_ordered = True  
                product_to_change.change_product_is_order_placed(is_ordered)
            else:
                print("Invalid")
                continue
        elif x == "q":
            break
        else:
            continue
            
    elif section == "b":
        x = input("What do you want to do? \n a to add new product \n c to change a product \n q quite\n")
        if x == "a":
            user_product_name = input("Enter the product name ")
            user_product_price = float(input("Enter the product price "))
            user_product_seller = input("Enter the product seller ")
            user_product_delivery_date = input("Enter the product delivery date ")
            
            product_1 = BuyingProduct(user_product_name, user_product_price
                                       , user_product_seller, user_product_delivery_date)
            buying_products.append(product_1)
              
        elif x == "c":
            products_we_have = len(buying_products)
            
            if products_we_have == 0:
                print("We have no Products, please add products ")
                continue
            
            print("We have " + str(products_we_have) + " Products")
            product_id = int(input("Which one to change? ")) 
            
            if products_we_have < product_id:
                print("Invalid product number ")
                continue
            
            product_to_change = buying_products[product_id - 1]
            
            to_change = input("What do you want to change? n for name, p for price, \n s for seller, and d for delivery date ")
            
            if to_change == "n":
                new_name = input("Enter the product name ")
                product_to_change.change_product_name(new_name)
            elif to_change == "p":
                new_price = float(input("Enter the product name "))
                product_to_change.change_product_price(new_price)
            elif to_change == "s":
                new_seller = input("Enter the seller name ")
                product_to_change.change_product_seller_name(new_seller)
            elif to_change == "d":
                new_delivery_date = int(input("Enter the delivery date "))
                product_to_change.change_product_delivery_date(new_delivery_date)
            else:
                print("Invalid")
                continue
    
                
        elif x == "q":
            break
        else:
            continue
    
    elif section == "q":
        break   
    else:
        print("invalid choice")
        continue
    


    
    
    
# -*- coding: utf-8 -*-
"""
@author:    Amir Tosson
@license:   GNU General Public License v3 or higher
@copyright: Universität Siegen, Deutschland
@email:     tosson@physik.uni-siegen.de   
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
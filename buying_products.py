# -*- coding: utf-8 -*-
"""
@author:    Amir Tosson
@license:   GNU General Public License v3 or higher
@copyright: Universität Siegen, Deutschland
@email:     tosson@physik.uni-siegen.de   
"""



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
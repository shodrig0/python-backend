from classes.product import Product
from classes.price import Price
from classes.branch import Branch
from classes.cart import Cart
from typing import List
from datetime import datetime


price1 = Price(220, datetime.now())
product1 = Product(1, 'Milk', 333443, 100, [price1])
branch1 = Branch(1, 'Manhattan','USA-2393', [product1])

price2 = Price(150, datetime.now())
product2 = Product(2, 'Milk', 338943, 2, [price2])
branch2 = Branch(2, 'New York','USA-2353', [product2])

price3 = Price(237, datetime.now())
product3 = Product(3, 'Milk', 243443, 100, [price3])
branch3 = Branch(3, 'Detroit','USA-2193', [product3])

price4 = Price(97, datetime.now())
product4 = Product(4, 'Milk', 333471, 100, [price4])
branch4 = Branch(4, 'Kansas','USA-9393', [product4])

specialProduct = Product(6, 'Chocolate', 44221, 5, [price1])

product5 = Product(5, 'Milk', 3321123, 100, [price2])
branch5 = Branch(5, 'Georgia', 'USA-1192', [product5, specialProduct])

# Lists for later
product_list: List[Product] = [product1, product2, product3, product4, product5, specialProduct]
price_list: List[Price] = [price1, price2, price3, price4]
branch_list: List[Branch] = [branch1, branch2, branch3, branch4, branch5]

cart1 = Cart()
print("STOCK: ", product2.stock)
print("-----------")
print ("PRICE: ", product2.price[0].value)
print("-----------")
print(f"Branch from { branch5.city } has { len(branch5.product) } products.")
print("-----------")
print(cart1.add(product2.stock, product2))
print("-----------")

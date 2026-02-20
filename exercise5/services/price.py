from models.price import Price

def create_price(amount, valid_from , valid_to, product_branch):
    price = Price(amount = amount, valid_from = valid_from, valid_to = valid_to, product_branch = product_branch)
    return price
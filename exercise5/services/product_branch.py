from models.product_branch import ProductBranch

def define_product_branch(product, branch, stock):
    product_branch = ProductBranch(product = product, branch = branch, stock = stock)
    return product_branch
from models.branch import Branch

def create_branch(city, postal_code):
    branch = Branch(city = city, postal_code = postal_code)
    return branch
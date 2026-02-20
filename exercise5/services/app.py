from services.initializer import initializer, session
from services.branch import create_branch
from services.product import create_product, get_all_products, get_product_by_description
from services.product_branch import define_product_branch
from services.price import create_price
from datetime import datetime, timezone

def app():
    initializer()

    new_branch = create_branch(city = 'NY', postal_code = 'NY-123')
    new_product = create_product('Strawberry Cookies', '09897')
    new_product_branch = define_product_branch(product = new_product, branch = new_branch, stock = 100)
    new_price = create_price(amount = 21, valid_from = datetime.now(timezone.utc), valid_to = None, product_branch = new_product_branch)

    session.add_all([new_branch, new_product, new_product_branch, new_price])

    session.commit()
    session.close()

    products = get_all_products()
    print(products)

    product_description = get_product_by_description('Cookies')
    print(product_description)

    print('Done')
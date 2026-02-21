from services.initializer import initializer, session
from services.branch import create_branch, get_product_by_postal_code
from services.product import create_product, get_all_products, get_products_by_description, order_product_by_description, update_description_product, get_product_by_sku, delete_product_by_sku
from services.product_branch import define_product_branch, group_products_branch
from services.price import create_price
from datetime import datetime, timezone

def app():
    initializer()

    # new_branch = create_branch(city = 'NY', postal_code = 'NY-123')
    # new_product = create_product('Blueberry Cookies', '55678')
    # insert_product_branch = group_products_branch('55678', 'NY-123', 150)
    new_price = create_price('55678', 'NY-123', 20, valid_from = datetime.now(timezone.utc), valid_to = None)
    # delete_product = delete_product_by_sku('55678')
    
    session.commit()

    session.close()

    print('Done')
# from services.initializer import initializer, session
# from services.branch import create_branch, get_product_by_postal_code
# from services.product import create_product, get_all_products, get_products_by_description, order_product_by_description, update_description_product, get_product_by_sku, delete_product_by_sku
# from services.product_branch import define_product_branch, group_products_branch
# from services.price import create_price, update_price
# from datetime import datetime, timezone

# def app():
#     initializer()

#     # Instances
#     # new_branch = create_branch(city = 'Kansas', postal_code = 'K-133')
#     # new_product = create_product('Chooolate Cookies', '5556')
#     # insert_product_branch = group_products_branch('4598', 'NY-123', 150)
#     # new_price = create_price('55678', 'NY-123', 20, valid_from = datetime.now(timezone.utc), valid_to = None)
#     # update_new_price = update_price('4598', 'NY-123', 30)

#     # To use this app() is necessary update services functions (remove session: Session and import from services.initializer import session)
    
#     session.commit()

#     session.close()

#     print('Done')

# app()
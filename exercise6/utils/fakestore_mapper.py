def fakestore_mapper(product: dict):
    mapped_product = {
        "sku": str(product["id"]),
        "title": product["title"],
        "description": product["description"],
        "image": product["image"],
        "category_name": product["category"],
        "price": product["price"]
    }

    return mapped_product
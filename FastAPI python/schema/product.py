def productEntity(product) -> dict:
    return {
        "id":str(product["id"]),
        "name": product["name"],
        "price": product["price"],
        "qty": product["qty"]
    }

def productsEntity(products) ->list:
    return [productEntity(product) for product in products]
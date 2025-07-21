def create_product(products,product_collection):
    new_product = products.model_dump()
    try:
        res = product_collection.insert_one(new_product)
    except Exception as e:
        return {"error":e},401
    finally:
        print(products)
    return {"id":str(res.inserted_id)}
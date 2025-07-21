from fastapi.responses import JSONResponse


def create_product(products, product_collection):
    # Inserts a new product into the products collection.

    # Args:
    #     products (Products): A validated Pydantic model containing product data.
    #     product_collection (Collection): A PyMongo collection object for 'products'.

    # Returns:
    #     tuple: A JSON-compatible dict with either:
    #         - On success: {"id": str(inserted_id)}, 201
    #         - On failure: {"error": Exception}, 500

    new_product = products.model_dump()
    try:
        res = product_collection.insert_one(new_product)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    finally:
        print(products)
    return JSONResponse(status_code=201, content={"id": str(res.inserted_id)})

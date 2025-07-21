from fastapi.responses import JSONResponse

def create_order(orders,order_collection):
    # Creates a new order and inserts it into the MongoDB 'orders' collection.

    # Args:
    #     orders (Orders): A Pydantic model instance containing order data.
    #     order_collection (Collection): The MongoDB collection where the order should be stored.

    # Returns:
    #     JSONResponse:
    #         - 201 Created: If the order is successfully inserted. Returns the inserted ID.
    #         - 500 Internal Server Error: If there is an exception during insertion. Returns the error message.

    new_orders = orders.model_dump()
    try:
        res = order_collection.insert_one(new_orders)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error":str(e)})
    finally:
        print(orders)
    return JSONResponse(status_code=201, content={"id":str(res.inserted_id)})
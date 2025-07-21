def create_order(orders,order_collection):
    new_orders = orders.model_dump()
    try:
        res = order_collection.insert_one(new_orders)
    except Exception as e:
        return {"error":e},401
    finally:
        print(orders)
    return {"id":str(res.inserted_id)}
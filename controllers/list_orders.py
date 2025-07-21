def post_processing_orders(doc):
    doc["id"] = str(doc.pop("_id"))
    doc.pop("userId", None)
    return doc


def list_orders(userId,params,order_collection,):
    query = {"userId": userId}
    params = params.model_dump()
    offset = params["offset"]
    limit = params["limit"]
    try:
        cursor = (
            order_collection.find(query)
            .sort("_id")
            .limit(limit)
            .skip(offset)
            
        )
        orders = [post_processing_orders(o) for o in cursor]
        return {
            "data": orders,
            "page": {
                "limit": limit,
                "next": offset + limit,
                "previous": offset - limit,
            }
        }
    except Exception as e:
        return {"error":str(e)}


    
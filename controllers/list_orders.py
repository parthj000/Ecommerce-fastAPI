from fastapi.responses import JSONResponse


def post_processing_orders(doc):
    doc["id"] = str(doc.pop("_id"))
    doc.pop("userId", None)
    return doc


def list_orders(userId, params, order_collection):
    # Lists orders for a specific user from the MongoDB 'orders' collection.

    # Args:
    #     userId (str): The ID of the user whose orders are to be fetched.
    #     params (OrderFilters): A Pydantic model instance containing pagination parameters (`offset` and `limit`).
    #     order_collection (Collection): The MongoDB collection object for 'orders'.

    # Returns:
    #     JSONResponse:
    #         - 200 OK: Returns a paginated list of processed orders, along with pagination metadata.
    #         - 500 Internal Server Error: Returns the error message if the operation fails.

    query = {"userId": userId}
    params = params.model_dump()
    offset = params["offset"]
    limit = params["limit"]
    try:
        cursor = order_collection.find(query).sort("_id").limit(limit).skip(offset)
        orders = [post_processing_orders(o) for o in cursor]
        return JSONResponse(
            status_code=200,
            content={
                "data": orders,
                "page": {
                    "limit": limit,
                    "next": offset + limit,
                    "previous": offset - limit,
                },
            },
        )
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

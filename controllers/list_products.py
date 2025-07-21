from fastapi.responses import JSONResponse


def post_processing_product(doc):
    doc["id"] = str(doc.pop("_id"))
    doc.pop("sizes", None)
    return doc


def list_products(params, product_collection):

    # Retrieves a list of products from the MongoDB collection with optional filtering and pagination.

    # Filters:
    #     - Name search (case-insensitive substring match).
    #     - Size match within embedded `sizes` array.

    # Args:
    #     params (ProductFilters): A Pydantic model instance containing:
    #         - name (Optional[str]): Name search query.
    #         - size (Optional[str]): Size filter.
    #         - limit (int): Number of results to return.
    #         - offset (int): Number of results to skip.
    #     product_collection (Collection): MongoDB collection object for products.

    # Returns:
    #     JSONResponse:
    #         - 200 OK: Returns a paginated list of products matching the filter criteria.
    #         - 500 Internal Server Error: If any exception occurs during database operations.

    params_dict = params.model_dump()

    name = params_dict["name"]
    size = params_dict["size"]
    limit = params_dict["limit"]
    offset = params_dict["offset"]

    query = {}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes"] = {"$elemMatch": {"size": size}}

    try:
        print(query)
        cursor = product_collection.find(query).sort("_id").skip(offset).limit(limit)
        products = [post_processing_product(p) for p in cursor]

        pagination = {
            "next": offset + limit,
            "limit": limit,
            "previous": offset - limit,
        }

        return JSONResponse(
            status_code=200, content={"data": products, "page": pagination}
        )
    except Exception as e:
        print("Error:", e)
        return JSONResponse(status_code=500, content={"error": str(e)})

def post_processing_product(doc):
    doc["id"] = str(doc.pop("_id"))
    doc.pop("sizes", None)
    return doc



def list_products(params,product_collection):
    params_dict = params.model_dump()
    
    name = params_dict["name"]
    size = params_dict["size"]
    limit = params_dict["limit"]
    offset = params_dict["offset"]

    query = {}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes"] = {
            "$elemMatch": {
                "size": size
            }
        }


    try:
        print(query)
        cursor = (
            product_collection.find(query)
            .sort("_id")
            .skip(offset)
            .limit(limit)
        )
        products = [post_processing_product(p) for p in cursor]
        pagination = {
            "next":offset + limit,
            "limit":limit,
            "previous":offset-limit
        }
        
        
        return {"data": products,"page":pagination}
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}



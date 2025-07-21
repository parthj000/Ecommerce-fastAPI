from fastapi import FastAPI, Depends
from models.get_products import ProductFilters
from models.get_orders import OrderFilters
from models.order import Orders
from controllers.create_product import create_product
from controllers.create_order import create_order
from controllers.list_products import list_products
from controllers.list_orders import list_orders
from db import db_connect
from models.products import Products

app = FastAPI()
product_collection, order_collection = db_connect()


@app.post("/products")
def handle_products_post(products: Products):
    return create_product(products, product_collection)


@app.get("/products")
def get_list(params: ProductFilters = Depends()):
    return list_products(params, product_collection)


@app.post("/orders")
def post_orders(orders: Orders):
    return create_order(orders, order_collection)


@app.get("/orders/{userId}")
def get_orders(userId: str, params: OrderFilters = Depends()):
    return list_orders(userId, params, order_collection)

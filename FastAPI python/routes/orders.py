import json
from fastapi import APIRouter, Request
from config.db import conn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

order = APIRouter()
templates = Jinja2Templates(directory="templates")

# GET all Orders
@order.get("/orders/", response_class=HTMLResponse)
async def read_order(request: Request):
    print('get orders API called')
    orders = conn.cosmocloud.orders.find({})
    allorders = []
    for order in orders:
        print(order)
        ord = json.JSONEncoder().encode({
            "id": str(order["_id"]),
            "items":order["items"],
            "amount": order["amount"],
        })
        print(ord)
        allorders.append(ord)
    return json.JSONEncoder().encode({
        "allorders": allorders
    })

# place order
@order.post("/orders/")
async def create_order(request:Request):
    print("'create order API' Called")
    body = await request.body()
    order_data = json.loads(body)

    order_id = str(conn.cosmocloud.orders.insert_one(dict(order_data)).inserted_id)
    return {"message": "Order placed successfully", "order_id": order_id}

import json

from fastapi import APIRouter, Request
from models.product import Product
from config.db import conn
from schema.product import productEntity, productsEntity
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

product = APIRouter()
templates = Jinja2Templates(directory="templates")

@product.get("/products/", response_class=HTMLResponse)
async def read_product(request: Request):
    print('get products api called')
    products = conn.cosmocloud.products.find({})
    allProducts = []
    for product in products:
        print(product)
        prod = json.JSONEncoder().encode({
            "id": str(product["_id"]),
            "name":product["name"],
            "price": product["price"],
            "qty": product["qty"]
        })
        print(prod)
        allProducts.append(prod)
        print(product)
    # return templates.TemplateResponse( { "request":request, "allProducts":allProducts })
    return json.JSONEncoder().encode({
        "allProducts": allProducts
    })

# @product.test("/")
# async def test():
#     print()
#     print('test api called', end="")
#     print()
#     return {'success':True}

@product.post("/products/")
async def create_product(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    product = conn.cosmocloud.products.insert_one(dict(formDict))
    return {"success": True}


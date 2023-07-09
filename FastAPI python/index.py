from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routes.product import product
from routes.orders import order
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(product)
app.include_router(order)

product.mount("/static", StaticFiles(directory="static"), name="static")


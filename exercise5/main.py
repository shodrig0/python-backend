from fastapi import FastAPI
from services.initializer import initializer
from schemas.product import product_router
from schemas.branch import branch_router
from schemas.product_branch import product_branch_router
from schemas.price import price_router
from contextlib import asynccontextmanager
from models.product import Product
from models.branch import Branch
from models.price import Price
from models.product_branch import ProductBranch

@asynccontextmanager
async def lifespan(app: FastAPI):
    initializer()
    print('Database initialized')

    yield

    print('App shutting down')

app = FastAPI(lifespan = lifespan)

routers = [product_router, branch_router, product_branch_router, price_router]

for router in routers:
    app.include_router(router)

@app.get('/')
async def root():
    return { 'msg': 'Exercise 5!' }
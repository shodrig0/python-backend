from fastapi import FastAPI
from schemas.product import product_router

api = FastAPI()

routers = [product_router]

for router in routers:
    api.include_router(router)

@api.get('/')
async def root():
    return { 'Exercise 5!' }
from fastapi import FastAPI
from product import product_router
from branch import branch_router

app = FastAPI()

routers = [product_router, branch_router]

for router in routers:
    app.include_router(router)

@app.get("/")
async def root():
    return {"hello there"}

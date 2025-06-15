from fastapi import FastAPI
import productsearcher

app = FastAPI()

@app.get("/")
def ping():
    return {"message": "pong"}

@app.get("/searchproduct/{product_name}")
def searchproduct(product_name):
    return productsearcher.search_product(product_name)

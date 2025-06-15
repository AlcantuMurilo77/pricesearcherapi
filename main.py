from fastapi import FastAPI, Path, HTTPException
import product_searcher

app = FastAPI()

@app.get("/")
def ping():
    return {"message": "pong"}

@app.get("/searchproduct/{product_name}")
def searchproduct(product_name: str = Path(..., min_length=2, max_length=100, pattern="^[a-zA-Z0-9çãáéêíóõúâô ]+$")
):

    result = product_searcher.search_product(product_name)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    
    return result

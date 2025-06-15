from fastapi import FastAPI, Path, HTTPException, Query
from dotenv import load_dotenv
import os
import product_searcher
import email_sender

load_dotenv()


email_login = os.getenv("EMAIL")
email_password = os.getenv("PASSWORD")

app = FastAPI()

@app.get("/")
def ping():
    return {"message": "pong"}

@app.get("/searchproduct/{product_name}")
def searchproduct(product_name: str = Path(..., min_length=2, max_length=100, pattern="^[a-zA-Z0-9çãáéêíóõúâô ]+$"),
                email_destino: str = Query(..., min_length=5, regex=r"^[^@]+@[^@]+\.[^@]+$")
):

    result = product_searcher.search_product(product_name)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    
    email_sender.send_email(email_login, 
                            email_password, 
                            "Product Price Searcher", 
                            email_destino, 
                            "Product Prices Report", 
                            "message.txt", 
                            result["filename"])

    os.remove(result["filename"])
    
    return result

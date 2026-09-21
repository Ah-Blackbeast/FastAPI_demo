from fastapi import FastAPI
app = FastAPI()

@app.get("/user")

def get_users(limit:int=5, quantity: int=None ,price: int=None, name: str = None):
    return{
        "name": name,
        "price":price,
        "quantity": quantity,
        "max no of item get": limit
    }

# def get_users(limit:int=5):
#     return{
#         "no of quantity get(max value)":limit
#     }
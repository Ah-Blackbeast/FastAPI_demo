from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return{"message": "hello death"}

@app.get("/about")
def about():
    return{"about":"i am death that comes for every single one"}

@app.get("/price")
def price():
    return {"price": ["int", "float", "roaming"]}

@app.get("/users/{user_ID}")
def get_user(user_ID):
    return{"user id": user_ID}
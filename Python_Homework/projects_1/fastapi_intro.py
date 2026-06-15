from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return{"message": "Привіт! мій перший FastAPI сервер "}
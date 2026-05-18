from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"messagem:": "Hello World!"}

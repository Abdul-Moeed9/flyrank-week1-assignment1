from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
    return {"message": "welcome to my 1st assignment submission :)"}

@app.get("/health")
def health():
    return {"status": "ok"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return "OK"

@app.post("/message")
def receive_message(message :str):
    return message



# python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

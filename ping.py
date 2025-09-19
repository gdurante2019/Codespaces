from fastapi import FastAPI
import uvicorn

app = FastAPI(title="ping")

@app.get("/ping")

def ping():
    return "Pong!"


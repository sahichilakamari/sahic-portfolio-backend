from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Portfolio backend is running!"}

@app.get("/portfolio")
async def get_portfolio():
    with open("portfolio.json", "r") as f:
        data = json.load(f)
    return data

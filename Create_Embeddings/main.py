import uvicorn
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def index():
   return {"message": "Hello World"}
@app.get("/hello/{name}")
async def hello(name):
   return {"name": name}
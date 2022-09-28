from fastapi import FastAPI
from mahasiswaRouter import Mahasiswa_router

app = FastAPI()
@app.get("/")
async def hello()-> dict:
    return{
        "message" : "Hello World"
    }
app.include_router(Mahasiswa_router)
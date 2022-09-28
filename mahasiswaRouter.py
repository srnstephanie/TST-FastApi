from fastapi import APIRouter
from pydantic import BaseModel

class Mahasiswa(BaseModel):  #the data model    
    nim : int
    nama: str

Mahasiswa_router = APIRouter()

@Mahasiswa_router.get("/")
async def hello() -> dict :
    return {
        "message": "Hello World"
        }
        
Mahasiswa_list = []

@Mahasiswa_router.post("/mahasiswa")
async def addMahasiswa(mahasiswa: Mahasiswa) -> dict :
    Mahasiswa_list.append(mahasiswa)
    return {"message":"Success"}

@Mahasiswa_router.get("/mahasiswa")
async def getMahasiswa() -> dict:
    return {"mahasiswa": Mahasiswa_list}
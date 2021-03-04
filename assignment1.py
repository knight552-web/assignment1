from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder



app=FastAPI()

a=[]
class Name(BaseModel):
    studentname:str
    studentid:str
    age:int

@app.get("/")
def basic():
    return "Welcome"

@app.get("/student")
def det(name:Name):
    return a



@app.post("/information")
def name(name:Name):
    d=dict()
    nameenc=jsonable_encoder(name)
    f=nameenc['studentname']
    i= nameenc['studentid']
    age=nameenc['age']
    d.update({"studentname":f,
    "studentid":i,
    "studentage":age})
    a.append(d)
    return "registered"

@app.put("/information/{studentid}")
async def update_item(studentid:str,name:Name):
    update_item_enc=jsonable_encoder(name)
    for p in a:
        if p['studentid']==studentid:
             p['studentage']=23
    return a

@app.put("/information/age/{studentage}")
def del_item(studentage:str,name:Name):
    for p in a:
        if p['studentage']==studentage:
            a.remove(p)
    return a

from datetime import datetime
import databases, sqlalchemy, DateTime ,uuid
from fastapi import FastAPI
from sqlalchemy import engine
from pydantic import BaseModel,Field
from typing import List
import uvicorn

#Database
DATABASE_URL = "mysql://root:root@localhost:3306/pan_lab"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


users = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id",  sqlalchemy.String(64), primary_key=True),
    sqlalchemy.Column("username",  sqlalchemy.String(128)),
    sqlalchemy.Column("password",  sqlalchemy.String(128)),
    sqlalchemy.Column("first_name",  sqlalchemy.String(64)),
    sqlalchemy.Column("last_name",  sqlalchemy.String(64)),
    sqlalchemy.Column("gender",  sqlalchemy.CHAR),
    sqlalchemy.Column("create_at",  sqlalchemy.String(64)),
    sqlalchemy.Column("status",  sqlalchemy.CHAR),
    
)
engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)

## Models
class UserList(BaseModel):
    id          : str
    username    : str
    password    : str
    first_name  : str 
    last_name   : str
    gender      : str
    create_at   : str 
    status      : str 


class UserEntry(BaseModel):

    username    : str = Field(..., example = "LI")
    password    : str = Field(..., example = "sdsdd")
    first_name  : str = Field(..., example = "Li")
    last_name   : str = Field(..., example = "Lei")
    gender      : str = Field(..., example = "M")





app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def helloword():
    return {"hello"," what's your name"}


@app.get("/users", response_model= List[UserList])
async def find_all_users():
    query = users.select()
    return await database.fetch_all(query)

@app.post("/users",response_model= UserList)
async def register_user(user: UserEntry):
    gID = str(uuid.uuid1())
    gDate = str(datetime.now())
    query = users.insert().values(
        id = gID,
        username = user.username,
        password = user.password,
        first_name = user.first_name,
        last_name = user.last_name,
        gender = user.gender,
        create_at = gDate,
        status = "1"
    ) 

    await database.execute(query)

    return {
        "id": gID,
        **user.dict(),
        "create_at": gDate,
        "status" :"1"

    }






if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8088)

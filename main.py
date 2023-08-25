from fastapi import FastAPI,Request


app = FastAPI()















# @app.get("/")
# async def root():
#     return {"message": "Hello World"}



@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}


@app.get("/name/{first}")
async def names(first:str):
    return{'firstname':first}
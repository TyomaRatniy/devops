from fastapi import FastAPI


server = FastAPI()




@server.get("/", include_in_schema=False)
async def root():
    return {"message": "Hello World"}



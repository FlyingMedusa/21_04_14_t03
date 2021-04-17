from fastapi import FastAPI, Response, status
# from fastapi.responses import JSONResponse
import hashlib

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.get("/auth")
async def read_items():
    the_hash = hashlib.sha512( str( password ).encode("utf-8") ).hexdigest()
    the_pass_check = password_hash.split("&password_hash=",1)[1] 
    


# @app.get("/auth")
# async def read_items(password: str, password_hash: str):
#     the_hash = hashlib.sha512( str( password ).encode("utf-8") ).hexdigest()
#     the_pass_check = password_hash.split("&password_hash=",1)[1] 
#     if the_hash == the_pass_check:
#         return JSONResponse(status_code=status.HTTP_204_CREATED, content=item)
#     else:
#         return JSONResponse(status_code=status.HTTP_401_CREATED, content=item)
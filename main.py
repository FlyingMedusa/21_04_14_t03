from fastapi import FastAPI, Request, Response, status
import hashlib
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.get("/auth")
def decrypt(response: Response, password: str = '', password_hash: str = ''):
    encrypted_password = hashlib.sha512(password.encode("utf-8")).hexdigest()
    if password_hash == encrypted_password:
        response.status_code = status.HTTP_204_NO_CONTENT
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED
    return response

@app.put("/register")
def update_item(name: str, surname: str):
    json_compatible_item_data = jsonable_encoder(name)
    return JSONResponse(content=json_compatible_item_data)
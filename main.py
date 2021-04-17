from fastapi import FastAPI, Request, Response, status
import hashlib

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
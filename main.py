from fastapi import FastAPI, Request, Response, status
import hashlib
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import date, timedelta, datetime
import itertools



class User(BaseModel):
    name: str
    surname: str

class RegisteredUser():
    newid = itertools.count()

    def __init__(self, name, surname):
        self.id = next(RegisteredUser.newid)
        self.name = name
        self.surname = surname
        self.register_date = str(date.today())
        self.vaccination_date = self.generate_vacc_date()
    
    def generate_vacc_date(self):
        delay = len(self.name) + len(self.surname)
        vaccination_date = datetime.fromisoformat(self.register_date) + timedelta(days=10)
        return vaccination_date.date()
    
    def register_user(self):
        res = {
            "id": self.id,
            "name" : self.name,
            "surname" : self.surname,
            "register_date" : self.register_date,
            "vaccination_date" : self.vaccination_date
        }
        return res
 

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

@app.post("/register")
async def create_user(response: Response, user: User):

    result = RegisteredUser(user.name, user.surname)
    response.status_code = status.HTTP_201_CREATED

    return result.register_user()
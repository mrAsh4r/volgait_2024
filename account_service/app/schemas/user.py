from pydantic import BaseModel

class UserSignUp(BaseModel):
    lastName: str
    firstName: str
    username: str
    password: str

class UserSignIn(BaseModel):
    username: str
    password: str
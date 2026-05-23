from pydantic import BaseModel,Field,field_validator,model_validator
from typing import Optional
import re


class Employe(BaseModel):
    id  : int
    name : str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employe Name",
        examples='Firdosh Khan'
    )
    department : Optional[str] = 'General'
    salary : float =Field(
        ...,
        ge=1000
    )


class User(BaseModel):
    userName : str = Field(
        ...,
        description="Enter Username",
        min_length=2,
        max_length=40,
    )
    email : str = Field(..., pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    


class InstaUser(BaseModel):
    username : str
    
    @field_validator('username')
    def userNameLength(cls , v):
        if len(v) < 4 :
            raise ValueError("User Must be at least 4 Charecters")
        return v

class SignupData(BaseModel):
    username : str
    password : str
    confirm_Password : str
    
    @model_validator(mode='after')
    def passwordMatch(self):
        if self.password != self.confirm_Password :
            raise ValueError("Password Does Not Matched")
        return self
    
    
def LoginUser (username , password , confirmPassword):
    appuser= SignupData(username=username , password=password , confirm_Password=confirmPassword)
    mainUser = InstaUser(username=username)
    print(f"Welcome User {username}")
    
    
LoginUser("F" , "12345" , "12345")
    




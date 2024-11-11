from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from schemas.user import userEntity, usersEntity
from models.user import User
from config.db import conn
from datetime import timedelta
from datetime import datetime, timedelta

from typing import Optional
import jwt
from fastapi.security import OAuth2PasswordBearer

user = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "mysecretkey"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

   
    expire_timestamp = int(expire.timestamp())

    to_encode = data.copy()
    to_encode.update({"exp": expire_timestamp}) 

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = verify_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )
        return email
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

# Findin User Api
@user.get('/')
async def find_all_users():
    users_list = list(conn.data_save.datacare.find())  
    print(users_list)  
    return usersEntity(users_list)

# Create an User
@user.post('/')
async def create_user(user: User):
  
    hashed_password = pwd_context.hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password  
    
  
    result = conn.data_save.datacare.insert_one(user_dict)
    
   
    inserted_user = conn.data_save.datacare.find_one({"_id": result.inserted_id})
    
    return userEntity(inserted_user)

# 3. Login Credentials
@user.post("/login")
async def login(user: User):
   
    db_user = conn.data_save.datacare.find_one({"email": user.email})

    if db_user is None:
        raise HTTPException(status_code=400, detail="Invalid email or password")

   
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    
    access_token_expires = timedelta(hours=1)
    access_token = create_access_token(
        data={"sub": db_user["email"]},
        expires_delta=access_token_expires
    )

    return {"message": "Logged in successfully"}


# Logout Credentials
@user.post("/logout")
async def logout():
    return {"message": "Successfully logged out"}

# 5. Protected Api
@user.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}, you have access to this protected route."}


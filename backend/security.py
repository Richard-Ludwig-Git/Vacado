from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from pydantic import BaseModel
from os import getenv
from dotenv import load_dotenv
import jwt
from jwt.exceptions import InvalidTokenError
import backend.data_handling


security_router = APIRouter()
page = Jinja2Templates(directory="frontend")
outh2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
load_dotenv("env/.env")



def verify_pw(real_pw, hashed_pw):
    return pwd_context.verify(real_pw, hashed_pw)


def get_pw_hash(real_pw):
    return pwd_context.hash(real_pw)


def authenticate(username: str, real_pw: str):
    user = backend.data_handling.get_user(username)
    if not user:
        return False
    if not verify_pw(real_pw, user.hashed_password):
        return False
    return user

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    user_id: int
    user_name: str
    email: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM"))
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(outh2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=getenv("ALGORITHM"))
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = backend.data_handling.get_user(username=token_data.username)
    if not user:
        raise credentials_exception
    return user


@security_router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not verify_pw(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Password wrong")
    access_token_exp = timedelta(minutes=float(getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(data={"sub": user.user_name}, expires_delta=access_token_exp)
    return Token(access_token=access_token, token_type="bearer")

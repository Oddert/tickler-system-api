from datetime import datetime

import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.config import JWT_ALGORITHM, JWT_SECRET_KEY
from app.db import get_db

from schemas.user import APIUser
from schemas.auth import JWTContent

from models.user import UserModel

oath = OAuth2PasswordBearer(
    tokenUrl='/login',
    scheme_name='JWT',
)

def require_auth(db=Depends(get_db), token: str=Depends(oath)) -> APIUser:
    try:
        decoded_token = jwt.decode(
            token,
            key=JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )
        token_parsed = JWTContent(**decoded_token)

        if datetime.fromtimestamp(token_parsed.exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='JWT token expired.',
                headers={
                    'WWW-Authenticate': 'Bearer'
                },
            )
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Could not validate JWT authorisation.' + str(ex),
            headers={
                'WWW-Authenticate': 'Bearer'
            },
        )
    
    found_user = UserModel.find_by_username(db, token_parsed.sub)

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User does not exist.',
            headers={
                'WWW-Authenticate': 'Bearer'
            },
        )
    
    return APIUser(**found_user.to_json())

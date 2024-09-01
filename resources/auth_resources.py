# pylint: disable=broad-exception-caught
from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from loguru import logger
from sqlalchemy.orm import Session

from app.db import get_db

from security.hash import get_hashed_pwd, verify_hashed_pwd
from security.token import create_access_token, create_refresh_token

from schemas.user import AuthUserPost
from schemas.auth import APIToken

from utils.responses import RespondOk, RespondServerError

from models.user import UserModel

router = APIRouter()


@router.post('/signup')
# @router.post('/signup', response_model=APIUser)
def create_user(
    # response: Response,
    user: AuthUserPost,
    db: Session = Depends(get_db),
):
    """Creates a new user."""
    found_user = UserModel.find_by_username(db, user.username)

    if found_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='A user with this username already exists',
        )
        # return RespondBadRequest(
        #     message='A user with this username already exists.'
        # ).send(response)

    created_user = UserModel(
        username=user.username,
        password=get_hashed_pwd(user.password),
    )
    db.add(created_user)
    db.commit()
    db.flush()

    return RespondOk({'user': created_user.to_json()}).send()


@router.post('/login', response_model=APIToken)
def login_user(
    # response: Response,
    db: Session = Depends(get_db),
    form: OAuth2PasswordRequestForm = Depends(),
):
    """Logs a user in, returns an access_token and refresh_token."""
    found_user = UserModel.find_by_username(db, form.username)

    if not found_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email or password.',
        )
        # return RespondBadRequest(
        #     message='Incorrect email or password.'
        # ).send(response)

    verified = verify_hashed_pwd(form.password, found_user.password)

    if not verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Incorrect email or password.',
        )
        # return RespondBadRequest(
        #     message='Incorrect email or password.'
        # ).send(response)

    return {
        'access_token': create_access_token(found_user.username),
        'refresh_token': create_refresh_token(found_user.username),
    }


@router.get('/user-exists/{username}')
def user_exists(
    username: str,
    response: Response,
    db: Session = Depends(get_db),
):
    '''Queries if a user exists.'''
    try:
        exists = UserModel.validate_username(db, username)
        return RespondOk(payload={'exists': exists}).send(response)
    except Exception as ex:
        logger.warning(str(ex))
        return RespondServerError({'message': str(ex)}).send(response)


@router.get('/user')
def temp(db: Session = Depends(get_db)):
    """Debug route to return all users"""
    return UserModel.find_all(db)

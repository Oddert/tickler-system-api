"""Utility functions for creating and refreshing JWTs."""

from datetime import datetime, timedelta
from typing import Any

import jwt

from app.config import (
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_ALGORITHM,
    JWT_REFRESH_SECRET_KEY,
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
)


def create_access_token(username: str | Any, expires_delta: int = None) -> str:
    """
    Generates a JWT access token, binding a username or other 'sub' parameter.

    Parameters:
    username: The username or other sub detail to bind.
    expires_delta: (Optional) Days till token expiry.

    Returns:
    encoded_token: The JWT token string.
    """
    if expires_delta:
        expires = datetime.now() + timedelta(expires_delta)
    else:
        expires = datetime.now() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

    token = {
        'exp': expires,
        'sub': str(username),
    }
    encoded_token = jwt.encode(
        token,
        JWT_SECRET_KEY,
        JWT_ALGORITHM,
    )
    return encoded_token


def create_refresh_token(username: str | Any, expires_delta: int = None) -> str:
    """
    Generates a JWT refresh token, binding a username or other 'sub' parameter.

    Parameters:
    username: The username or other sub detail to bind.
    expires_delta: (Optional) Days till token expiry.

    Returns:
    encoded_token: The JWT token string.
    """
    if expires_delta:
        expires = datetime.now() + timedelta(expires_delta)
    else:
        expires = datetime.now() + timedelta(minutes=JWT_REFRESH_TOKEN_EXPIRE_MINUTES)

    token = {
        'exp': expires,
        'sub': str(username),
    }
    encoded_token = jwt.encode(
        token,
        JWT_REFRESH_SECRET_KEY,
        JWT_ALGORITHM,
    )
    return encoded_token

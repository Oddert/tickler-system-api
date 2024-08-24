from pydantic import BaseModel, Field

class APIUser(BaseModel):
    user_id: str=Field(
        ...,
        min_length=3,
        max_length=100,
        title='The user\'s unique ID.'
    )
    username: str=Field(
        ...,
        min_length=3,
        max_length=100,
        title='The user\'s unique username.'
    )

class AuthUserPost(BaseModel):
    username: str=Field(
        ...,
        min_length=3,
        max_length=100,
        title='The user\'s unique username.'
    )
    password: str=Field(
        ...,
        min_length=3,
        max_length=100,
        title='The user\'s password.'
    )

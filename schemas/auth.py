from pydantic import BaseModel, Field

class APIToken(BaseModel):
    access_token: str=Field(
        ...,
        min_length=3,
        max_length=125,
        title='The JWT access token.'
    )
    refresh_token: str=Field(
        ...,
        min_length=3,
        max_length=125,
        title='The JWT access token.'
    )

from fastapi import APIRouter, Depends, Response

from app.db import get_db

from security.middleware import require_auth

from utils.responses import RespondOk

from schemas.user import APIUser

from models.prompt import PromptModel

router = APIRouter()

@router.get('/prompt')
def get_all_prompts(
    response: Response,
    db=Depends(get_db),
    user: APIUser=Depends(require_auth)
):
    query = PromptModel.find_all(db)
    return RespondOk(payload=query).send(response)

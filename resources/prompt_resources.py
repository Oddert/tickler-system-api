from fastapi import APIRouter, Depends, Response

from app.db import get_db

from utils.responses import RespondOk

from models.prompt import PromptModel

router = APIRouter()

@router.get('/prompt')
def get_all_prompts(
    response: Response,
    db=Depends(get_db),
):
    query = PromptModel.find_all(db)
    print(query)
    return RespondOk().send(response)

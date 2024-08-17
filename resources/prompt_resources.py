from fastapi import APIRouter, Response

from utils.responses import RespondOk

router = APIRouter()

@router.get('/prompt')
def get_all_prompts(response: Response):
    return RespondOk().send(response)

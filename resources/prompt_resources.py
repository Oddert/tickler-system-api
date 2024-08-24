"""Handles all routes for /prompt."""

# pylint: disable=broad-exception-caught
from dateutil.parser import parse
from uuid import UUID

from fastapi import APIRouter, Depends, Response
from loguru import logger

from app.db import get_db

from security.middleware import require_auth

from utils.responses import (
    RespondNotFound,
    RespondOk,
    RespondUnauthorised,
    RespondServerError,
)

from schemas.prompt import PromptPost, PromptPut
from schemas.user import APIUser

from models.prompt import PromptModel

router = APIRouter()


@router.get('/prompt')
def get_all_prompts(  # pylint: disable = unused-variable
    response: Response,
    db=Depends(get_db),
    user: APIUser = Depends(require_auth),
):
    """Gets all prompts for a user."""
    query = PromptModel.find_all_by_username(db, user.username)
    prompts = [p.to_json() for p in query]
    return RespondOk(payload=prompts).send(response)


@router.post('/prompt')
def create_prompt_single(  # pylint: disable = unused-variable
    response: Response,
    prompt: PromptPost,
    db=Depends(get_db),
    user: APIUser = Depends(require_auth),
):
    """Creates a new prompt."""
    try:
        created_prompt = PromptModel(
            criticality=prompt.criticality,
            date=parse(prompt.date),
            defer_period=prompt.deferPeriod,
            defer_quantity=prompt.deferQuantity,
            description=prompt.description,
            # links=prompt.links,
            status=prompt.status,
            title=prompt.title,
            user_id=UUID(user.user_id),
        )

        db.add(created_prompt)

        db.commit()
        db.flush()

        return RespondOk({'prompt': created_prompt.to_json()}).send()

    except Exception as ex:
        logger.warning(str(ex))
        return RespondServerError({'error': str(ex)}).send(response)


@router.put('/prompt/{prompt_id}')
def update_prompt(  # pylint: disable = unused-variable
    response: Response,
    prompt: PromptPut,
    prompt_id: str,
    db=Depends(get_db),
    user: APIUser = Depends(require_auth),
):
    """Updates a prompt."""
    try:
        found_prompt: PromptModel = PromptModel.find_by_id(db, prompt_id)

        if not found_prompt:
            return RespondNotFound(
                {'message': 'No prompt with id "{prompt_id}" found.'}
            ).send(response)

        if UUID(user.user_id) != found_prompt.user_id:
            return RespondUnauthorised(
                {'message': 'You do not have permission to modify this prompt.'}
            ).send(response)

        created_prompt = PromptModel(
            criticality=prompt.criticality,
            date=parse(prompt.date),
            defer_count=prompt.deferCount,
            defer_period=prompt.deferPeriod,
            defer_quantity=prompt.deferQuantity,
            description=prompt.description,
            # links=prompt.links,
            status=prompt.status,
            title=prompt.title,
            user_id=UUID(user.user_id),
        )

        db.add(created_prompt)

        db.commit()
        db.flush()

        return RespondOk({'prompt': created_prompt.to_json()}).send()

    except Exception as ex:
        logger.warning(str(ex))
        return RespondServerError({'error': str(ex)}).send(response)

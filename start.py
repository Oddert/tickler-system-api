import uvicorn

from fastapi import FastAPI

from resources.prompt_resources import router as prompt_routes

# from app.config import port

from app.db import engine
from app.orm import ORMModelBase

server = FastAPI()

server.include_router(prompt_routes, prefix='/v0', tags=['Prompts'])

ORMModelBase.metadata.create_all(bind=engine, checkfirst=True)

if __name__ == '__main__':
    uvicorn.run(
        'start:server',
        reload=True,
        # port=port if port else '8001'
    )

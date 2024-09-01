import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from resources.auth_resources import router as auth_routes
from resources.prompt_resources import router as prompt_routes

# from app.config import port

from app.db import engine
from app.orm import ORMModelBase

server = FastAPI()

server.include_router(prompt_routes, prefix='/v0', tags=['Prompts'])
server.include_router(auth_routes, tags=['Auth'])

origins = [
    'http://localhost:3000',
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ORMModelBase.metadata.create_all(bind=engine, checkfirst=True)

if __name__ == '__main__':
    uvicorn.run(
        'start:server',
        reload=True,
        # port=port if port else '8001'
    )

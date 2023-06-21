from random import randint
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from graph_router import graphql_app as graph_router
from rest_router import router as rest_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(rest_router)
app.include_router(graph_router, prefix="/graphql")
from fastapi import FastAPI
from app.api import alert, rule, role, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.include_router(rule.router, prefix="/rule")
app.include_router(role.router, prefix="/role")
app.include_router(user.router, prefix="/user")
app.include_router(alert.router, prefix="/alert")
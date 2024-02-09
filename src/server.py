from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from routers.chats import chats_router
from routers.users import users_router

from routers.auth import auth_router
from routers.registration import registration_router

from sql_base.base import base_worker

BASE_PATH = 'db.db'
base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    print("БД не существует")
    base_worker.create_base('../sql/base.sql')
else:
    print("БД существует")
    
app = FastAPI()

# CORS
origins = [
    "http://localhost:3000",  # адрес клиентского приложения
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main_page():
    return {'page': 'Connection in correct'}
    
app.include_router(chats_router, prefix='/chats') # post('http://127.0.0.1:8000/login', json=data)
app.include_router(users_router, prefix='/users')

app.include_router(auth_router, prefix='/auth')
app.include_router(registration_router, prefix='/registration')

PORT = 8000
HOST = "127.0.0.1"

if __name__ == "__main__":
    uvicorn.run("server:app", port=PORT, host=HOST, reload=True)
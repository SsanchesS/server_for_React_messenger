from fastapi import APIRouter
from src.models import LoginM
from src.resolvers.auth import check_login_request

auth_router = APIRouter()

@auth_router.post('/')
def f_auth(user:LoginM):
    user = check_login_request(user)
    if user == 500:
        return {"code": 500, "message": "Ошибка сервера","user":None}
    if user is None:
        return {"code": 401, "message": "email или password не верны, попробуй снова","user":None}
    return {"code": 200, "message": "Ты вошёл",'user': user}
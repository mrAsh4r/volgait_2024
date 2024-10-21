from fastapi import APIRouter
from ..schemas.user import UserSignUp, UserSignIn  # Импорт схем
from fastapi import HTTPException

router = APIRouter()

@router.post("/api/Authentication/SignUp", summary="Регистрация нового аккаунта")
async def sign_up(user: UserSignUp):
    # Логика регистрации
    return {"message": "User created"}

@router.post("/api/Authentication/SignIn", summary="Получение новой пары JWT")
async def sign_in(user: UserSignIn):
    # Логика аутентификации
    return {"access_token": "jwt_token", "token_type": "bearer"}

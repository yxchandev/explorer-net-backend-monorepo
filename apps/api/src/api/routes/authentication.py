"""Authentication routes."""

from fastapi import APIRouter

from api.controllers import authentication as auth_controller
from api.controllers.authentication import (
    AuthResponse,
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    ResetPasswordRequest,
)

router = APIRouter(prefix="/authentication", tags=["authentication"])


@router.post("/login", response_model=AuthResponse)
def login(body: LoginRequest) -> AuthResponse:
    return auth_controller.login(body)


@router.post("/register", response_model=AuthResponse)
def register(body: RegisterRequest) -> AuthResponse:
    return auth_controller.register(body)


@router.post("/forgotpassword", response_model=AuthResponse)
def forgot_password(body: ForgotPasswordRequest) -> AuthResponse:
    return auth_controller.forgot_password(body)


@router.post("/resetpassword", response_model=AuthResponse)
def reset_password(body: ResetPasswordRequest) -> AuthResponse:
    return auth_controller.reset_password(body)

"""Authentication routes."""

from fastapi import APIRouter

from apps.consumer.src.controllers import authentication
from packages.pylib.src.models.consumer.authentication import (
    AuthResponse,
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    ResetPasswordRequest,
)

router = APIRouter(prefix="/authentication", tags=["authentication"])


@router.post("/login", response_model=AuthResponse)
def login(body: LoginRequest) -> AuthResponse:
    return authentication.login(body)


@router.post("/register", response_model=AuthResponse)
def register(body: RegisterRequest) -> AuthResponse:
    return authentication.register(body)


@router.post("/forgotpassword", response_model=AuthResponse)
def forgot_password(body: ForgotPasswordRequest) -> AuthResponse:
    return authentication.forgot_password(body)


@router.post("/resetpassword", response_model=AuthResponse)
def reset_password(body: ResetPasswordRequest) -> AuthResponse:
    return authentication.reset_password(body)

"""Consumer authentication controllers."""

from pylib.models.consumer.authentication import (
    AuthResponse,
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    ResetPasswordRequest,
)
from pylib.services import authentication as auth_service


def login(body: LoginRequest) -> AuthResponse:
    result = auth_service.login(email=body.email, password=body.password)
    return AuthResponse.model_validate(result)


def register(body: RegisterRequest) -> AuthResponse:
    result = auth_service.register(
        email=body.email,
        password=body.password,
        name=body.name,
    )
    return AuthResponse.model_validate(result)


def forgot_password(body: ForgotPasswordRequest) -> AuthResponse:
    result = auth_service.forgot_password(email=body.email)
    return AuthResponse.model_validate(result)


def reset_password(body: ResetPasswordRequest) -> AuthResponse:
    result = auth_service.reset_password(
        token=body.token,
        new_password=body.new_password,
    )
    return AuthResponse.model_validate(result)

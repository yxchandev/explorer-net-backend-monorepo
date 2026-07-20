"""Consumer authentication controllers."""

from packages.pylib.src.models.consumer.authentication import (
    AuthResponse,
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    ResetPasswordRequest,
)
from packages.pylib.src.services import authentication


def login(body: LoginRequest) -> AuthResponse:
    result = authentication.login(email=body.email, password=body.password)
    return AuthResponse.model_validate(result)


def register(body: RegisterRequest) -> AuthResponse:
    result = authentication.register(
        email=body.email,
        password=body.password,
        name=body.name,
    )
    return AuthResponse.model_validate(result)


def forgot_password(body: ForgotPasswordRequest) -> AuthResponse:
    result = authentication.forgot_password(email=body.email)
    return AuthResponse.model_validate(result)


def reset_password(body: ResetPasswordRequest) -> AuthResponse:
    result = authentication.reset_password(
        token=body.token,
        new_password=body.new_password,
    )
    return AuthResponse.model_validate(result)

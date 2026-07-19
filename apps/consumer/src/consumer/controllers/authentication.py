"""Authentication controllers with Pydantic request/response models."""

from pydantic import BaseModel, Field

from pylib.services import authentication as auth_service


class LoginRequest(BaseModel):
    email: str = Field(min_length=1)
    password: str = Field(min_length=1)


class RegisterRequest(BaseModel):
    email: str = Field(min_length=1)
    password: str = Field(min_length=8)
    name: str = Field(min_length=1)


class ForgotPasswordRequest(BaseModel):
    email: str = Field(min_length=1)


class ResetPasswordRequest(BaseModel):
    token: str = Field(min_length=1)
    new_password: str = Field(min_length=8)


class AuthResponse(BaseModel):
    status: str
    message: str
    email: str | None = None
    name: str | None = None
    token: str | None = None


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

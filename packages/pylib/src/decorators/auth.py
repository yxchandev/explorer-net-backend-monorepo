"""Authentication decorators for FastAPI routes."""

from __future__ import annotations

import inspect
from collections.abc import Callable
from functools import wraps
from typing import Any, ParamSpec, TypeVar

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from packages.pylib.src.utils.auth import verify_access_token

P = ParamSpec("P")
R = TypeVar("R")

_bearer_scheme = HTTPBearer(auto_error=True)


def _authenticate(
    credentials: HTTPAuthorizationCredentials = Depends(_bearer_scheme),
) -> dict[str, Any]:
    try:
        return verify_access_token(credentials.credentials)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def require_jwt(func: Callable[P, R]) -> Callable[P, R]:
    """Require a valid JWT Bearer token on the decorated route."""

    @wraps(func)
    def wrapper(
        *args: P.args,
        __jwt_payload__: dict[str, Any] = Depends(_authenticate),
        **kwargs: P.kwargs,
    ) -> R:
        return func(*args, **kwargs)

    original = inspect.signature(func)
    jwt_param = inspect.Parameter(
        "__jwt_payload__",
        inspect.Parameter.KEYWORD_ONLY,
        default=Depends(_authenticate),
        annotation=dict[str, Any],
    )
    wrapper.__signature__ = original.replace(  # type: ignore[attr-defined]
        parameters=[*original.parameters.values(), jwt_param],
    )
    return wrapper  # type: ignore[return-value]

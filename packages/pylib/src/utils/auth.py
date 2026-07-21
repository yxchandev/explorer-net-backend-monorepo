"""JWT access-token helpers."""

from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

_DEFAULT_ALGORITHM = "HS256"
_DEFAULT_EXPIRE_MINUTES = 60


def _require_secret() -> str:
    secret = os.getenv("JWT_SECRET")
    if not secret:
        raise ValueError("JWT_SECRET is missing. Set it in the environment or .env file.")
    return secret


def _algorithm() -> str:
    return os.getenv("JWT_ALGORITHM", _DEFAULT_ALGORITHM)


def generate_access_token(
    payload: dict[str, Any],
    *,
    expires_delta: timedelta | None = None,
) -> str:
    """Create a signed JWT access token from ``payload``."""
    to_encode = payload.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta
        if expires_delta is not None
        else timedelta(
            minutes=int(
                os.getenv(
                    "JWT_ACCESS_TOKEN_EXPIRE_MINUTES",
                    str(_DEFAULT_EXPIRE_MINUTES),
                )
            )
        )
    )
    to_encode["exp"] = expire
    return jwt.encode(to_encode, _require_secret(), algorithm=_algorithm())


def verify_access_token(token: str) -> dict[str, Any]:
    """Decode and validate a JWT access token. Raises on failure."""
    decoded = jwt.decode(
        token,
        _require_secret(),
        algorithms=[_algorithm()],
    )
    return dict(decoded)

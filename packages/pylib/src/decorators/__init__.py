"""Shared FastAPI decorators."""

from packages.pylib.src.decorators.auth import require_jwt

__all__ = ["require_jwt"]

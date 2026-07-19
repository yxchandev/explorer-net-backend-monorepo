"""PostgreSQL connection helpers (sync and async)."""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager, contextmanager

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import Session, sessionmaker

_sync_engines: dict[str, Engine] = {}
_async_engines: dict[str, AsyncEngine] = {}


def _require_url(url: str | None, env_name: str) -> str:
    resolved = url or os.getenv(env_name)
    if not resolved:
        raise ValueError(
            f"Database URL missing. Pass database_url or set {env_name}."
        )
    return resolved


def get_sync_engine(database_url: str | None = None) -> Engine:
    """Get (or create) a sync SQLAlchemy engine for PostgreSQL."""
    url = _require_url(database_url, "DATABASE_URL")
    engine = _sync_engines.get(url)
    if engine is None:
        engine = create_engine(url, pool_pre_ping=True)
        _sync_engines[url] = engine
    return engine


def get_async_engine(database_url: str | None = None) -> AsyncEngine:
    """Get (or create) an async SQLAlchemy engine for PostgreSQL."""
    url = _require_url(database_url, "ASYNC_DATABASE_URL")
    engine = _async_engines.get(url)
    if engine is None:
        engine = create_async_engine(url, pool_pre_ping=True)
        _async_engines[url] = engine
    return engine


def connect(database_url: str | None = None) -> Session:
    """Open a sync DB session. Caller must close it (or use session_scope)."""
    engine = get_sync_engine(database_url)
    factory = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
        expire_on_commit=False,
    )
    return factory()


async def connect_async(database_url: str | None = None) -> AsyncSession:
    """Open an async DB session. Caller must close it (or use async_session_scope)."""
    engine = get_async_engine(database_url)
    factory = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        autoflush=False,
        expire_on_commit=False,
    )
    return factory()


@contextmanager
def session_scope(database_url: str | None = None) -> Iterator[Session]:
    """Sync session context manager with commit/rollback."""
    session = connect(database_url)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


@asynccontextmanager
async def async_session_scope(
    database_url: str | None = None,
) -> AsyncIterator[AsyncSession]:
    """Async session context manager with commit/rollback."""
    session = await connect_async(database_url)
    try:
        yield session
        await session.commit()
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

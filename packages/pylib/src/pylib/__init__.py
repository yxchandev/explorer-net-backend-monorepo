"""Shared library used by workspace apps."""

from pylib.greeting import greet
from pylib.services import authentication, consumer, discovery

__all__ = ["greet", "authentication", "consumer", "discovery"]

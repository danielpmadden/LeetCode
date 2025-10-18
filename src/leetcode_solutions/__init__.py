"""Top-level package for curated LeetCode solutions."""

from importlib import resources as _resources
from pathlib import Path as _Path

PACKAGE_ROOT = _Path(__file__).resolve().parent
"""Path to the installed package directory."""

__all__ = ["PACKAGE_ROOT"]

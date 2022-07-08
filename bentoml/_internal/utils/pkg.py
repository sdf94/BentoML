from __future__ import annotations

from types import ModuleType

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

from packaging.version import Version

__all__ = ["pkg_version_info", "get_pkg_version"]

get_pkg_version = importlib_metadata.version


def pkg_version_info(pkg_name: str | ModuleType) -> tuple[int, int, int]:
    if isinstance(pkg_name, ModuleType):
        pkg_name = pkg_name.__name__
    pkg_version = Version(get_pkg_version(pkg_name))
    return pkg_version.major, pkg_version.minor, pkg_version.micro

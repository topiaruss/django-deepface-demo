from django import template
from django.core.cache import cache
import subprocess
from functools import lru_cache
import tomllib
import os

register = template.Library()


@lru_cache(maxsize=1)
def get_git_commit():
    """Get the short git commit hash."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.SubprocessError, FileNotFoundError):
        return "unknown"


@lru_cache(maxsize=1)
def get_version():
    """Get the version from pyproject.toml."""
    try:
        # Get the project root directory (where pyproject.toml is located)
        project_root = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        pyproject_path = os.path.join(project_root, "pyproject.toml")

        with open(pyproject_path, "rb") as f:
            pyproject = tomllib.load(f)
            return pyproject["project"]["version"]
    except (FileNotFoundError, KeyError, tomllib.TOMLDecodeError):
        return "unknown"


@register.simple_tag
def version_info():
    """Return version information for display in templates."""
    cache_key = "version_info"
    version_info = cache.get(cache_key)

    if version_info is None:
        version = get_version()
        commit = get_git_commit()
        version_info = f"v{version} ({commit})"
        cache.set(cache_key, version_info, timeout=3600)  # Cache for 1 hour

    return version_info

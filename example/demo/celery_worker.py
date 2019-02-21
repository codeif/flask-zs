from . import create_app
from .core import celery as app

create_app()

__all__ = (
    'app',
)

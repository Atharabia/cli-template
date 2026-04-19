from typer import Typer

from .version import VersionHandler

handlers = [
    VersionHandler,
]


def load_handlers(app: Typer) -> None:
    for handler_cls in handlers:
        handler_cls(app)

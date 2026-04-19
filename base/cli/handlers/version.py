import typer

from cli.base.handler import HandlerBase
from cli.commands.version import VersionCommand


class VersionHandler(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        @self.command.command(
            name="version",
            help="Display version information",
        )
        def version() -> None:
            VersionCommand().version()

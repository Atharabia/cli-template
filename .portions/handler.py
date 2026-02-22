import typer

from cli.base import HandlerBase
from cli.commands import COMMAND_CLASS_NAME


class COMMAND_HANDLER_NAME(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        COMMAND_VAR_NAME = COMMAND_CLASS_NAME()

        @self.command.command()
        def COMMAND_FUNCTION_NAME() -> None:
            COMMAND_VAR_NAME.add()

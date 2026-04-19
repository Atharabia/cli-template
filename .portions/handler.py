import typer

from cli.base.handler import HandlerBase
from cli.commands.COMMAND_NAME import COMMAND_CLASS_NAME


class HANDLER_CLASS_NAME(HandlerBase):
    def __init__(self, app: typer.Typer) -> None:
        super().__init__(app)

    def register_commands(self) -> None:
        @self.command.command(
            name="HANDLER_FUNCTION_NAME",
            help="HANDLER_FUNCTION_HELP",
        )
        def HANDLER_FUNCTION_NAME() -> None:
            COMMAND_CLASS_NAME().HANDLER_FUNCTION_NAME()

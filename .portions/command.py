import typer

from cli.base import CommandBase


class COMMAND_CLASS_NAME(CommandBase):
    def __init__(self) -> None:
        super().__init__()

    def register(self, app: typer.Typer) -> None:
        @app.command()
        def COMMAND_FUNCTION_NAME() -> None:
            self.COMMAND_FUNCTION_NAME()

    def COMMAND_FUNCTION_NAME(self) -> None:
        ...

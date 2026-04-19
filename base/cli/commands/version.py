from importlib.metadata import version

from cli.base import CommandBase
from cli.models import Message


class VersionCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()

    def version(self) -> None:
        self.terminal.info(Message.Version.DISPLAY,
                           version=version("cli-template"))

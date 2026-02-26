from typing import Dict

from cli.core import Terminal


class CommandBase:
    def __init__(self, **kwargs: Dict[str, str]) -> None:
        self.logger = Terminal(quiet=False)

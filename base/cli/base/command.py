from cli.core.terminal import Terminal


class CommandBase:
    def __init__(self) -> None:
        self.terminal = Terminal()

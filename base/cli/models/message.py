from dataclasses import dataclass


@dataclass
class Message:
    @dataclass
    class Version:
        DISPLAY = "Cli Template: {version}"

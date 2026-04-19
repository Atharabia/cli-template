from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    verbose: bool = False
    auto_confirm: bool = False

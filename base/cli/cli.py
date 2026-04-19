import typer

from cli.handlers import load_handlers
from cli.models import Config


class Cli:
    def __init__(self) -> None:
        self.cli = typer.Typer(callback=self.callback,
                               add_completion=True,
                               help="CLI Template",
                               no_args_is_help=True)

    def callback(self,
                 verbose: bool = typer.Option(False,
                                              "-v",
                                              help="Enable verbose mode"),
                 auto_confirm: bool = typer.Option(False,
                                                   "-y",
                                                   help="Auto Confirm"),
                 ) -> None:
        Config.verbose = verbose
        Config.auto_confirm = auto_confirm

    def run(self) -> None:
        load_handlers(self.cli)
        self.cli()

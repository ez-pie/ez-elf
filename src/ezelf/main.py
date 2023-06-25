import typer

from .sync import ezpie

app = typer.Typer()


@app.callback()
def callback():
    """
    Ez-elf is a convenient script for ezpie, which provides:

    - package code and save to ezpie.
    """


@app.command()
def save_my_dir(dir_path: str = None, include_hidden: bool = False):
    """
    Pack the contents of given directory and save it to ezpie.
    """
    if dir_path is None:
        ezpie.copy_working_dir(include_hidden)
    else:
        ezpie.copy_dir(dir_path, include_hidden)

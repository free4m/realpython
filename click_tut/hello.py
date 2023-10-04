import click
from pathlib import Path


@click.command("hello")
@click.version_option("0.1.0", prog_name="hello")
def hello():
    click.echo("Hello, Danguses!")


if __name__ == "__main__":
    hello()

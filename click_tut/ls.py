import click
from pathlib import Path
from datetime import datetime

# v1
# @click.command()
# @click.argument("path")
# def cli(path):
#     target_dir = Path(path)
#     if not target_dir.exists():
#         click.echo("The target director does not exist.")
#         raise SystemExit(1)
    
#     for entry in target_dir.iterdir():
#         click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

#     click.echo()

# v2
# @click.command()
# @click.argument(
#     "path",
#     type=click.Path(
#         exists=True,
#         file_okay=False,
#         readable=True,
#         path_type=Path,
#     ),
# )
# def cli(path):
#     for entry in path.iterdir():
#         click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)

#     click.echo()


# v3
# @click.command()
# @click.argument(
#     "paths",
#     nargs=-1,
#     type=click.Path(
#         exists=True,
#         file_okay=False,
#         readable=True,
#         path_type=Path,
#     ),
# )
# def cli(paths):
#     for i, path in enumerate(paths):
#         if len(paths) > 1:
#             click.echo(f"{path}/:")
#         for entry in path.iterdir():
#             click.echo(f"{entry.name:{len(entry.name) + 5}}", nl=False)
#         if i < len(paths) - 1:
#             click.echo("\n")
#         else:
#             click.echo()


# v4
@click.command()
@click.option("-l", "--long", is_flag=True)
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(
        exists=True,
        file_okay=False,
        readable=True,
        path_type=Path,
    ),
    help="Display the directory content in long format."
)
def cli(paths, long):
    """List the content of one or more directories.

    PATHS is one or more directory paths whose content will be listed.
    """
    for i, path in enumerate(paths):
        if len(paths) > 1:
            click.echo(f"{path}/:")
        for entry in  path.iterdir():
            entry_output = build_output(entry, long)
            click.echo(f"{entry_output:{len(entry_output) + 5}}", nl=long)
        if i < len(paths) - 1:
            click.echo("" if long else "\n")
        elif not long:
            click.echo()

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.fromtimestamp(entry.stat().st_mtime)
        return f"{size:>6d} {date:%b %d %H:%M:%S} {entry.name}"
    return entry.name


if __name__ == "__main__":
    cli()

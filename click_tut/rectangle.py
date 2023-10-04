import click

# v1
# @click.command()
# @click.option("--size", nargs=2, type=click.INT)
# def cli(size):
#     width, height = size
#     click.echo(f"size: {size}")
#     click.echo(f"{width} x {height}")


# v2
@click.command()
@click.option("--size", type=(click.INT, click.INT))
# @click.option("--size", type=click.Tuple([int, int]))
def cli(size):
    width, height = size
    click.echo(f"size: {size}")
    click.echo(f"{width} x {height}")   


if __name__ == "__main__":
    cli()

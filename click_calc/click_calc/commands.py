import click


@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    """
    Add two numbers.
    """
    click.echo(a + b)

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def sub(a, b):
    """
    Subtract two numbers.
    """
    click.echo(a - b)

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def mul(a ,b):
    """
    Multiply two numbers.
    """
    click.echo(a * b)

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def div(a, b):
    """
    Divide two numbers.
    """
    click.echo(a / b)

import click


@click.group()
def cli():
    """Program obsługujący różne komendy."""
    pass


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def add(a, b):
    """Dodawanie dwóch liczb."""
    click.echo(f"Wynik: {a + b}")


@cli.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
def multiply(a, b):
    """Mnożenie dwóch liczb."""
    click.echo(f"Wynik: {a * b}")


@cli.command()
@click.argument("c", type=int)
@click.argument("d", type=int)
def power(c: int, d: int):
    """Potęgowanie dwóch liczb."""
    click.echo(f"Wynik: {c**d}")


if __name__ == "__main__":
    cli()

# Uruchamianie
# python script.py add 2 3
# python script.py multiply 4 5

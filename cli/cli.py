import click

from modules.balance import balanceOf
from modules.detail import detail
from modules.holders import holders
from modules.latest_transaction import latest_transaction
from modules.watch import watch






@click.group()
def cli():
    pass


cli.add_command(detail)
cli.add_command(balanceOf)
cli.add_command(watch)
cli.add_command(latest_transaction)
cli.add_command(holders)

if __name__ == "__main__":
    cli()

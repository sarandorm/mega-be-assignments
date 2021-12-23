import click

from utils import get_latest_transaction


@click.command(name="latest_tx")
@click.argument("number")
@click.argument("contract_address")
def latest_transaction(number,contract_address):
    '''Get n latest transaction on the contract address into a text file'''
    get_latest_transaction(number,contract_address)
    click.echo("Get latest transaction successfully!")
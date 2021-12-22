import click

from utils import get_latest_transaction, get_top_holder_in_contract

@click.command(name="holders")
@click.argument("number")
@click.argument("contract_address")
def holders(number,contract_address):
    '''Get top n token holders address and balance on the contract address'''
    get_top_holder_in_contract(number,contract_address)
    click.echo('Get holder successfully!')
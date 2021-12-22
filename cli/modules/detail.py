import click
from web3.exceptions import ContractLogicError
from requests.exceptions import HTTPError
from utils import convert_to_check_sum_address, initiate_contact,contract_decimals,contract_name,contract_symbol


@click.command(name='detail')
@click.argument('contract_address')
def detail(contract_address):
    '''Get contract address symbol, name and decimals'''
    try:
        contract = initiate_contact(convert_to_check_sum_address(contract_address))
        click.echo(f'Contract Symbol : {contract_symbol(contract)}')
        click.echo(f'Contract Name : {contract_name(contract)}')
        click.echo(
            f'Contract Decimals : {contract_decimals(contract)}')
    except ContractLogicError:
        click.echo("Contract address not in ERC20")
    except HTTPError:
        click.echo("Invalid URL")
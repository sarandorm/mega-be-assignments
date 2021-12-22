import click
from web3.exceptions import ContractLogicError

from func import contract_symbol, contract_target_balance, initiate_contact



@click.command(name='balance')
@click.argument('contract_address')
@click.argument('target_address')
def balanceOf(contract_address, target_address):
    try:
        contract = initiate_contact(contract_address)
        balance = contract_target_balance(contract,target_address)
        click.echo(f'Balance : {balance} {contract_symbol(contract)}')
    except ContractLogicError:
        click.echo("Contract address not in ERC20")
    except ValueError:
        click.echo('Invalid address')
import click
from web3.exceptions import ContractLogicError

from func import convert_to_check_sum_address, create_filter

@click.command(name='watch')
@click.argument('contract_address')
def watch(contract_address):
    try:
        filter = create_filter(convert_to_check_sum_address(contract_address))
        while True:
            cache = ''
            for log in filter.get_new_entries():
                if log["transactionHash"].hex() != cache:
                    print(f'https://etherscan.io/tx/{ log["transactionHash"].hex()}')
                cache = log["transactionHash"].hex()
    except KeyboardInterrupt:
        pass
    except ValueError:
        click.echo('Invalid address')
    except ContractLogicError:
        click.echo("Contract address not in ERC20")
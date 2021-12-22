import json
import os
from dotenv import load_dotenv
from eth_utils import address
import requests
from eth_typing.evm import Address
from web3 import Web3
from web3_input_decoder import decode_constructor, decode_function

with open('abi.json', 'r') as j:
    abi = json.loads(j.read())

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv('INFURA_URL')))

etherscan_api_key = os.getenv('ETHERSCAN_API_KEY')

ethplorer_api_key = os.getenv('ETHPLORER_API_KEY')




def convert_to_check_sum_address(address):
    return Web3.toChecksumAddress(address)


def initiate_contact(contract_address):
    address = convert_to_check_sum_address(contract_address)
    return w3.eth.contract(address=address, abi=abi)


def contract_symbol(contract):
    return contract.functions.symbol().call()


def contract_decimals(contract):
    return contract.functions.decimals().call()


def contract_name(contract):
    return contract.functions.name().call()


def contract_target_balance(contract, target_address):
    address = convert_to_check_sum_address(target_address)
    return contract.functions.balanceOf(address).call() / 10 ** contract_decimals(contract)


def create_filter(address):
    return w3.eth.filter({"block": "latest", "address": Web3.toChecksumAddress(address)})

def get_transaction_input(contract,transaction_hash):
    hex_string = w3.eth.get_transaction(transaction_hash)['input']
    try:
        func_obj,func_params = contract.decode_function_input(hex_string)
        return str(func_obj).strip('<>').split(' ')[1]
    except ValueError:
        return ('fail')
    



def get_latest_transaction(n, contract_address):
    payload = { 
                'module': 'account', 
                'action': 'tokentx',
                'contractaddress': contract_address, 
                "sort": "asc", 
                "apikey": etherscan_api_key
                }
    print(etherscan_api_key)
    count = 0
    file = open("latest_transaction.txt",'w')
    response = requests.get('https://api.etherscan.io/api', params=payload)
    contract = initiate_contact(contract_address)
    for i in response.json()["result"]:
        if int(n) > count:
            file.write("Sender address : " + i["from"] + " ")
            file.write("Transaction hash : " + i["hash"] + " ")
            function = get_transaction_input(contract,i['hash'])
            if function == 'fail' :
                file.write('Function not in ABI')
            else:
                file.write("Function name : " + function)
            file.write('\n')
            count += 1
        else:
            break
    file.close()

def get_top_holder_in_contract(n, contract_address):
    payload = {
        "limit":n,
        "apiKey":ethplorer_api_key
    }
    file = open("top_holder.txt",'w')
    response = requests.get(f'https://api.ethplorer.io/getTopTokenHolders/{contract_address}',params=payload)
    print(response)
    for i in response.json()['holders']:
        file.write( 'Address :' + i['address'] + ' ' + 'Balance :' + str(i['balance']))
        file.write('\n')
    file.close()


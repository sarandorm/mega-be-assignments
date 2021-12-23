# CLI part
## Setting up credentials

You need to setup environment files (.env) as in the template_env
```
ETHERSCAN_API_KEY=
ETHPLORER_API_KEY=
INFURA_URL=
```
You can get the API key from etherscan and ethplorer via their API pages

Get the Infura url from Infura dashboard

## Command

Here are all commands of this program

```
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  balance    Get balance of the target address on the contract address
  detail     Get contract address symbol, name and decimals
  holders    Get top n token holders address and balance on the contract...
  latest_tx  Get n latest transaction on the contract address into a text...
  watch      Subscribe to transaction and return etherscan link for that...
```

## Example 

```
cli.py detail 0xB8c77482e45F1F44dE1745F52C74426C631bDD52
```
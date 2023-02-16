from web3 import Web3

infura_url = "https://celo-mainnet.infura.io/v3/7be3ca45a0744e49a63063053fb43d73"

web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if the connection is established
print(web3.isConnected())

# Get the latest block number
print(web3.eth.blockNumber)

# Get the balance of an address
address = "0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9"
balance = web3.eth.getBalance(address)

# Convert the balance from wei to ether
ether_balance = web3.fromWei(balance, "ether")

# Print the result
print(ether_balance)

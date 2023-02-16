from web3 import Web3

ganach_url = "http://127.0.0.1:8545"
web3=Web3(Web3.HTTPProvider(ganach_url))

# Check if the connection is established
print(web3.isConnected())

account_1 = "0x8313f2bEff0af4C8582497e97bc4f6638eE6C053"
account_2= "0xe401F96e72b3414aF420f42F89993B49d5C75095"

private_key="6a580061139c5da909d0919b5f9e21a3681ccdb83b4fa47b9425404b573871cd"

nonace=web3.eth.getTransactionCount(account_1)

# Create a transaction

tx = {
    'nonce': nonace,
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# Sign the transaction

signed_tx = web3.eth.account.signTransaction(tx, private_key)

# Send the transaction

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# Get the transaction hash

print(web3.toHex(tx_hash))

# Get the transaction receipt

print(web3.eth.waitForTransactionReceipt(tx_hash))

# Get the balance of the second account

print(web3.eth.getBalance(account_2))

# Get the balance of the first account

print(web3.eth.getBalance(account_1))
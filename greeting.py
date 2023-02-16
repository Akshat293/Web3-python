from web3 import Web3
import json

ganach_url = "http://127.0.0.1:8545"
web3=Web3(Web3.HTTPProvider(ganach_url))

web3.eth.defaultAccount = web3.eth.accounts[0]
abi=json.loads('[{"inputs":[],"name":"getGreeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address= web3.toChecksumAddress("0xd8BCDbf8b85f86C5f6e862A1E074f3d7f70F6E5E")

contract = web3.eth.contract(address=address, abi=abi)
string = contract.functions.getGreeting().call()
print(string)

tx_hash=contract.functions.setGreeting("Hello World 123").transact()


web3.eth.waitForTransactionReceipt(tx_hash)

string = contract.functions.getGreeting().call()
print(string)

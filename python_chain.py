from web3 import Web3

# Connect to an Ethereum node
web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # Replace with your Ethereum node URL

# Load the contract ABI and bytecode
contract_abi = [...]  # Insert ABI here
contract_bytecode = '0x...'  # Insert bytecode here

# Deploy the contract
SimpleStorage = web3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)
tx_hash = SimpleStorage.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

# Get the deployed contract address
contract_address = tx_receipt.contractAddress

# Create contract instance
simple_storage = web3.eth.contract(address=contract_address, abi=contract_abi)

# Set data
tx_hash = simple_storage.functions.setData(42).transact()
web3.eth.wait_for_transaction_receipt(tx_hash)

# Get data
data = simple_storage.functions.getData().call()
print("Data stored in the contract:", data)

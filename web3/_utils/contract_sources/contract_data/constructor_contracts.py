"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.18.
"""

# source: web3/_utils/contract_sources/ConstructorContracts.sol:SimpleConstructorContract  # noqa: E501
SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE = "0x6080604052348015600f57600080fd5b50603f80601d6000396000f3fe6080604052600080fdfea2646970667358221220b0f7f5c19ff1398e836d0dfe7c50fdbabf6f411ba0220e07bdc307ec345d282564736f6c63430008120033"  # noqa: E501
SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME = "0x6080604052600080fdfea2646970667358221220b0f7f5c19ff1398e836d0dfe7c50fdbabf6f411ba0220e07bdc307ec345d282564736f6c63430008120033"  # noqa: E501
SIMPLE_CONSTRUCTOR_CONTRACT_ABI = [
    {"inputs": [], "stateMutability": "nonpayable", "type": "constructor"}
]
SIMPLE_CONSTRUCTOR_CONTRACT_DATA = {
    "bytecode": SIMPLE_CONSTRUCTOR_CONTRACT_BYTECODE,
    "bytecode_runtime": SIMPLE_CONSTRUCTOR_CONTRACT_RUNTIME,
    "abi": SIMPLE_CONSTRUCTOR_CONTRACT_ABI,
}


# source: web3/_utils/contract_sources/ConstructorContracts.sol:ConstructorWithArgumentsContract  # noqa: E501
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE = "0x608060405234801561001057600080fd5b50604051610214380380610214833981810160405281019061003291906100b8565b816000819055508060018190555050506100f8565b600080fd5b6000819050919050565b61005f8161004c565b811461006a57600080fd5b50565b60008151905061007c81610056565b92915050565b6000819050919050565b61009581610082565b81146100a057600080fd5b50565b6000815190506100b28161008c565b92915050565b600080604083850312156100cf576100ce610047565b5b60006100dd8582860161006d565b92505060206100ee858286016100a3565b9150509250929050565b61010d806101076000396000f3fe6080604052348015600f57600080fd5b506004361060325760003560e01c806388ec1346146037578063d4c46c76146051575b600080fd5b603d606b565b60405160489190608e565b60405180910390f35b60576071565b6040516062919060be565b60405180910390f35b60005481565b60015481565b6000819050919050565b6088816077565b82525050565b600060208201905060a160008301846081565b92915050565b6000819050919050565b60b88160a7565b82525050565b600060208201905060d1600083018460b1565b9291505056fea2646970667358221220e03f788db6a6c8ceeedb0402274149af0465b0c51cbf20a3d3caf4dcf8edeb3e64736f6c63430008120033"  # noqa: E501
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME = "0x6080604052348015600f57600080fd5b506004361060325760003560e01c806388ec1346146037578063d4c46c76146051575b600080fd5b603d606b565b60405160489190608e565b60405180910390f35b60576071565b6040516062919060be565b60405180910390f35b60005481565b60015481565b6000819050919050565b6088816077565b82525050565b600060208201905060a160008301846081565b92915050565b6000819050919050565b60b88160a7565b82525050565b600060208201905060d1600083018460b1565b9291505056fea2646970667358221220e03f788db6a6c8ceeedb0402274149af0465b0c51cbf20a3d3caf4dcf8edeb3e64736f6c63430008120033"  # noqa: E501
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI = [
    {
        "inputs": [
            {"internalType": "uint256", "name": "a", "type": "uint256"},
            {"internalType": "bytes32", "name": "b", "type": "bytes32"},
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [],
        "name": "data_a",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "data_b",
        "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}],
        "stateMutability": "view",
        "type": "function",
    },
]
CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_DATA = {
    "bytecode": CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_BYTECODE,
    "bytecode_runtime": CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_RUNTIME,
    "abi": CONSTRUCTOR_WITH_ARGUMENTS_CONTRACT_ABI,
}


# source: web3/_utils/contract_sources/ConstructorContracts.sol:ConstructorWithAddressArgumentContract  # noqa: E501
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE = "0x608060405234801561001057600080fd5b5060405161020d38038061020d833981810160405281019061003291906100db565b806000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050610108565b600080fd5b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b60006100a88261007d565b9050919050565b6100b88161009d565b81146100c357600080fd5b50565b6000815190506100d5816100af565b92915050565b6000602082840312156100f1576100f0610078565b5b60006100ff848285016100c6565b91505092915050565b60f7806101166000396000f3fe6080604052348015600f57600080fd5b506004361060285760003560e01c806334664e3a14602d575b600080fd5b60336047565b604051603e919060a8565b60405180910390f35b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000609482606b565b9050919050565b60a281608b565b82525050565b600060208201905060bb6000830184609b565b9291505056fea2646970667358221220728ed63fbb3b63b844a135b64314f2d4817d4d374f0d9b5181116ad53c5a744464736f6c63430008120033"  # noqa: E501
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME = "0x6080604052348015600f57600080fd5b506004361060285760003560e01c806334664e3a14602d575b600080fd5b60336047565b604051603e919060a8565b60405180910390f35b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600073ffffffffffffffffffffffffffffffffffffffff82169050919050565b6000609482606b565b9050919050565b60a281608b565b82525050565b600060208201905060bb6000830184609b565b9291505056fea2646970667358221220728ed63fbb3b63b844a135b64314f2d4817d4d374f0d9b5181116ad53c5a744464736f6c63430008120033"  # noqa: E501
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI = [
    {
        "inputs": [{"internalType": "address", "name": "_testAddr", "type": "address"}],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "inputs": [],
        "name": "testAddr",
        "outputs": [{"internalType": "address", "name": "", "type": "address"}],
        "stateMutability": "view",
        "type": "function",
    },
]
CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_DATA = {
    "bytecode": CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_BYTECODE,
    "bytecode_runtime": CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_RUNTIME,
    "abi": CONSTRUCTOR_WITH_ADDRESS_ARGUMENT_CONTRACT_ABI,
}

from block import Block
from transaction import Transaction
from blockchain import Blockchain
import time

if __name__ == "__main__":
    blockchain = Blockchain(4)
    transaction = Transaction('A', 'B', 100)
    # Create a new block
    block = Block(transaction, blockchain.get_last_block(), blockchain.get_new_index())
    # Add the block to the blockchain
    blockchain.add_block(block)
    

    print(blockchain.is_chain_valid())
    # Print the block's hash
    print(blockchain.chain)
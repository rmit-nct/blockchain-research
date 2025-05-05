from block import Block
from transaction import Transaction
import time

if __name__ == "__main__":
    transaction = Transaction('A', 'B', 100)
    # Create a new block
    block = Block(transaction, 'asdfaf', 0 )
    
    # Mine the block with a difficulty of 4
    block.mine_block(4)
    
    print(block.data)
    # Print the block's hash
    print(f"Block hash: {block.hash}")
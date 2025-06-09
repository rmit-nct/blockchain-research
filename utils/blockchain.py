from utils.transaction import Transaction
from utils.block import Block

class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.chain.append(self.create_genesis_block())

    def create_genesis_block(self):
        genesis_transaction = Transaction("none", "none", 0)
        return Block(genesis_transaction, "", 0)

    def get_last_block(self):
        return self.chain[-1]
    def get_new_index(self):
        return len(self.chain)
    def get_difficulty(self):
        return self.difficulty

    def add_block(self, new_block):
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
    
    def print_chain(self):
        for block in self.chain:
            print("-" * 40)
            print(f"Index: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Sender: {block.data.sender}")
            print(f"Receiver: {block.data.receiver}")
            print(f"Amount: {block.data.amount}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print(f"Nonce: {block.nonce}")

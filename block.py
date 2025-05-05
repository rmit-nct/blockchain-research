import hashlib

class Block():
    def __init__(self, transaction, previous_hash, index):
        """
        Initialize a new block with the given parameters.
        :param index: The index of the block in the blockchain.
        :param previous_hash: The hash of the previous block.
        :param timestamp: The time when the block was created.
        :param data: The data contained in the block.
        """
        # Initialize the block's attributes
        # index, previous_hash, timestamp, nonce, data, hash
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = transaction.timestamp
        self.nonce = 0
        self.data = transaction
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Compute the hash of the block using its attributes.
        :return: The hash of the block as a hexadecimal string.
        """
        
        # Compute the hash of the block using its attributes
        return hashlib.sha256(f"{self.index}{self.previous_hash}{self.timestamp}{self.nonce}{self.data}".encode()).hexdigest()
    
    
    def mine_block(self, difficulty):
        """
        Mine the block by finding a hash that starts with a certain number of zeros.
        :param difficulty: The number of leading zeros required in the hash.
        """
        # Increment nonce until the hash of the block starts with the required number of zeros
        prefix_str = '0' * difficulty
        while self.hash[:difficulty] != prefix_str:
            self.nonce += 1
            self.hash = self.compute_hash()
        
        print(f"Block mined: {self.nonce},  {self.hash}")
        return self.hash
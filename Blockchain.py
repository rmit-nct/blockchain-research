class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.chain.append(self.create_genesis_block())

    def create_genesis_block(self):
        genesis_transactions = [Transaction("none", "none", 0)]
        return Block(0, genesis_transactions, "0")

    def get_last_block(self):
        return self.chain[-1]

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
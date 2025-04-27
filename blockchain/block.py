import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value_to_hash = (
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previous_hash) +
            str(self.nonce)
        )
        return hashlib.sha256(value_to_hash.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Proof of Work: hash must start with 'difficulty' number of zeros
        required_prefix = '0' * difficulty
        while not self.hash.startswith(required_prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

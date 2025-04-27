from blockchain.block import Block


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Start simple: 2 leading zeros required

    def create_genesis_block(self):
        return Block(index=0, data="Genesis Block", previous_hash="0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=previous_block.index + 1,
            data=new_data,
            previous_hash=previous_block.hash
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

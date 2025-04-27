import unittest
from blockchain.blockchain import Blockchain


class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        genesis_block = self.blockchain.chain[0]
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(genesis_block.data, "Genesis Block")
        self.assertEqual(genesis_block.previous_hash, "0")

    def test_add_block(self):
        self.blockchain.add_block("Test Block 1")
        self.blockchain.add_block("Test Block 2")

        self.assertEqual(len(self.blockchain.chain), 3)  # Genesis + 2 blocks

        latest_block = self.blockchain.get_latest_block()
        self.assertEqual(latest_block.data, "Test Block 2")
        self.assertEqual(
            latest_block.previous_hash,
            self.blockchain.chain[-2].hash
        )

    def test_chain_validation(self):
        self.blockchain.add_block("Block A")
        self.blockchain.add_block("Block B")

        is_valid = self.blockchain.is_chain_valid()
        self.assertTrue(is_valid)

        # Tamper with the blockchain
        self.blockchain.chain[1].data = "Hacked Data"

        is_valid_after_tampering = self.blockchain.is_chain_valid()
        self.assertFalse(is_valid_after_tampering)


if __name__ == '__main__':
    unittest.main()

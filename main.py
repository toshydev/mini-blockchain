from blockchain.blockchain import Blockchain


def main():
    my_blockchain = Blockchain()

    print("Mining block 1...")
    my_blockchain.add_block("First block data")

    print("Mining block 2...")
    my_blockchain.add_block("Second block data")

    print("\nBlockchain:")
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("-" * 30)

    print("Blockchain valid?", my_blockchain.is_chain_valid())


if __name__ == "__main__":
    main()

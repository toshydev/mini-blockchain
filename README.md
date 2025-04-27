# Mini Blockchain

A minimal blockchain simulator built in Python to understand basic blockchain concepts like blocks, hashing, proof of work, and chain validation.

![Python Tests](https://github.com/toshydev/mini-blockchain/actions/workflows/python-tests.yml/badge.svg)

## Features

-   Create a chain of blocks
-   Each block stores:
    -   Index
    -   Timestamp
    -   Data
    -   Previous block's hash
    -   Its own hash
-   Simple Proof of Work (adjustable difficulty)
-   Chain validation logic

## Project Structure

```plaintext
mini-blockchain/
├── blockchain/
│   ├── block.py         # Block class: defines structure and hashing
│   └── blockchain.py    # Blockchain class: manages the chain
├── main.py              # Demo: create and print the blockchain
├── tests/
│   └── test_blockchain.py  # (optional) Basic unit tests
├── README.md
└── requirements.txt
```

## How to Run

1. Clone this repository:

    ```bash
    git clone https://github.com/toshydev/mini-blockchain.git
    cd mini-blockchain
    ```

2. (Optional) Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies (for testing):

    ```bash
    pip install -r requirements.txt
    ```

4. Run the blockchain demo:
    ```bash
    python main.py
    ```

## Example Output

```plaintext
Mining block 1…
Mining block 2…

Blockchain:
Index: 0
Timestamp: 1681234567.123456
Data: Genesis Block
Previous Hash: 0
Hash: 000a1b2c3d…

Index: 1
Timestamp: 1681234570.123456
Data: First block data
Previous Hash: 000a1b2c3d…
Hash: 0004f6e7f8…

…
Blockchain valid? True
```

## Future Improvements

-   Add transaction objects inside blocks
-   Network simulation with multiple nodes
-   More advanced consensus algorithms (Proof of Stake, BFT)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

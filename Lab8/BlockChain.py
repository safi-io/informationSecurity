import hashlib
import time

# Step 1: Define the Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index  # Position of the block in the chain
        self.timestamp = timestamp  # Time of creation
        self.data = data  # Data stored in the block
        self.previous_hash = previous_hash  # Hash of the previous block in the chain
        self.hash = self.compute_hash()  # Current block's hash based on its contents

    # Step 2: Compute SHA-256 hash of the block (excluding self.hash)
    def compute_hash(self):
        # Concatenate all relevant fields as a single string
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    # Representation for printing
    def __str__(self):
        return f"Block #{self.index}\nTimestamp: {self.timestamp}\nData: {self.data}\nPrevious Hash: {self.previous_hash}\nHash: {self.hash}\n"


# Example: Create the genesis block (first block in the chain)
genesis_block = Block(0, time.time(), "Genesis Block", "0")

# Output the details of the block
print(genesis_block)

#!/usr/bin/env python

# An mvp implementation of a blockchain

import hashlib

class Block(object):
    """Single block of a blockchain

    Parameters
    ----------
    data : object
        data for the block to contain
    previousHash : str
        hash of previous block on chain

    Attributes
    ----------
    data : object
        data of the object
    previousHash : str
        hash of previous block
    hash : str
        hash of current block

    """
    def __init__(self, previousHash, data):
        self.previousHash = previousHash
        self.data = data
        self.hash = self.computeHash()

    def computeHash(self):
        """Compute hash of current block
        """
        # Convert data to byte string
        data = str(self.data).encode('ASCII')
        # Convert previous hash to byte string
        previousHash = str(self.previousHash).encode('ASCII')
        # Get the hash of the current block
        return hashlib.sha256(data + previousHash).hexdigest()

    def __str__(self):
        return 'data: {}\nPreviousHash: {}\nHash: {}\n'.format(self.data, self.previousHash, self.hash)

class BlockChain(object):
    """Basic implementation of a blockchain

    Attributes
    ----------
    chain : iterable
        a chain of blocks
    """
    def __init__(self):
        # Must initialize the genesis block with default data
        self.chain = []
        self.chain.append(Block('0', 'Genesis block'))

    def get_latest(self):
        """Get the latest block in the chain
        """
        return self.chain[-1]

    def add(self, data):
        """Add a new block to the chain
        """
        # Get latest block from chain
        old = self.get_latest()
        # Create a new block with hash of the previous block and data
        new = Block(old.hash, data)
        self.chain.append(new)

    def __str__(self):
        """Print the chain
        """
        rep = ''
        for item in self.chain:
            rep += str(item)
        return rep

if __name__ == '__main__':
    bc = BlockChain()
    bc.add(5)
    bc.add(4)
    print(bc)

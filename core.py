import datetime
import hashlib
import random

class Block:
    blockNo = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def getdata(self):
        return self.data

    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
         return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nPokemon Name: " + str(self.data['name']) + "\nPokemon Level: " + str(self.data['level']) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    maxNonce = 2**32
    starters = ['Charmander', 'Bulbasaur', 'Squirtle']
    genesisPokemon = {
        'name': str(random.choice(starters)),
        'level': 1
    }
    block = Block(genesisPokemon)
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block, diff):
        target = 2** (256-diff)
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= target:
                self.add(block)
                print(block)
                return block
            else:
                block.nonce += 1

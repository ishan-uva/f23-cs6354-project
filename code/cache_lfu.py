import numpy as np
from math import log
import random


class Cache:

    def __init__(self, cSize, ways=2, bSize=4):
        
        self.cacheSize = cSize
        self.ways = ways
        self.blockSize = bSize
        self.sets = cSize // bSize // ways

        self.blockBits = 0
        self.setBits = 0

        if (self.blockSize != 1):
            self.blockBits = int(log(self.blockSize, 2))

        if (self.sets != 1):
            self.setBits = int(log(self.sets, 2))

        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=np.int64)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0

        print("=" * 20)
        print("Initializing CACHE w/ LEAST FREQUENTLY USED replacement. Properties include:")
        print("cacheSize:", self.cacheSize)
        print("ways:", self.ways)
        print("blockSize:", self.blockSize)
        print("sets:", self.sets)
        print("=" * 20)


    def reset(self):
        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=np.int64)
        self.cache = self.cache - 1

        self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64)
        self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        

    def find_set(self, address):
        return (address // self.blockSize) % self.sets

    
    def find_tag(self, address):
        return (address // self.blockSize) // self.sets


    def find(self, address):

        tag = self.find_tag(address)
        set_number = self.find_set(address)
        set_number = np.where(self.cache[set_number] == tag)
        if set_number[0].size > 0:
            self.hit += 1
            # Increment the frequency of the accessed block
            self.metaCache[self.find_set(address)] += 1
            return True
        else:
            self.miss += 1
            return False
        
   
    def load(self, address):
        set_number = self.find_set(address)
        tag = self.find_tag(address)
        if self.find(address):
            return
        else:
            # Find the block with the least frequency
            replacement_block = np.argmin(self.metaCache[set_number])
            # Replace the block with the new block
            self.cache[set_number][replacement_block // self.blockSize] = tag
            # Reset the frequency of the new block
            self.metaCache[set_number][replacement_block // self.blockSize] = 0


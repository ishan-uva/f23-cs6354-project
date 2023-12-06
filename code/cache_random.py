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

        # self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64)
        # self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0

        print("=" * 20)
        print("Initializing CACHE w/ RANDOM replacement. Properties include:")
        print("cacheSize:", self.cacheSize)
        print("ways:", self.ways)
        print("blockSize:", self.blockSize)
        print("sets:", self.sets)
        print("=" * 20)


    def reset(self):
        self.cache = np.zeros((self.sets, self.ways, self.blockSize), dtype=np.int64)
        self.cache = self.cache - 1

        # self.metaCache = np.zeros((self.sets, self.ways), dtype=np.int64)
        # self.metaCache = self.metaCache - 1

        self.hit = 0
        self.miss = 0
        

    def find_set(self, address):
        return (address // self.blockSize) % self.sets

    
    def find_tag(self, address):
        return (address // self.blockSize) // self.sets


    def find(self, address):

        s = self.find_set(address)
        t = self.find_tag(address)

        for i in range(len(self.cache[s])):

            if t != self.cache[s][i][0]:
                continue

            self.hit += 1
            return True

        self.miss += 1
        return False

   
    def load(self, address):

        if self.find(address):
            return

        s = self.find_set(address)
        t = self.find_tag(address)

        random_index = random.randint(0, len(self.cache[s]) - 1)

        self.cache[s][random_index] = [ t for _ in range(self.blockSize) ]
        # self.metaCache[s][random_index] = self.hit + self.miss + 1


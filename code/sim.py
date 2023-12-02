import sys
import os

from cache_lfu import Cache as CacheLFU
from cache_random import Cache as CacheRandom
from cache_lru import Cache as CacheLRU


if __name__ == "__main__":

    try:
        files = os.listdir("./traces/")
        cacheType = sys.argv[1]
        cacheSize = int(sys.argv[2])
        ways = int(sys.argv[3])
        block_size = int(sys.argv[4])

    except Exception as e:
        print("Please provide all the required parameters: 1 - Cache Type, 2 - Cache Size, 3 - Ways, 4 - Block Size", "\nError:", e)
        exit(0)

    if cacheType == "random":
        cache = CacheRandom(cacheSize, ways, block_size)
    elif cacheType == "lfu":
        cache = CacheLFU(cacheSize, ways, block_size)
    elif cacheType == "lru":
        cache = CacheLRU(cacheSize, ways, block_size)
    else:
        print("Please provide a valid cache type: [random, lfu, lru]")
        exit(0)

    cache.reset()

    for file in files:

        print(file)

        cache.reset()
        compute = 0

        with open(f"./traces/{file}") as f:
            trace = f.readlines()

        for t in range(len(trace)):

            if t % 1000 == 0:
                print("Processing the program trace, progress so far =", int(t / len(trace) * 100), "%")

            compute += int(trace[t].split(" ")[0])
            address = int(trace[t].split(" ")[1])

            found = cache.find(address)
            if found == False:
                cache.load(address)

            print("set and tag of", hex(address), "is", cache.find_set(address), cache.find_tag(address))
            if found:
                print("address", hex(address), "CACHE HIT. Good Job.")
            else:
                print("address", hex(address), "CACHE MISS. Loading from memory.")
        
        load_requests = len(trace)
        misses = load_requests - cache.hit
        miss_rate = misses / load_requests
        hit_rate = 1 - miss_rate

        print("total cache misses", misses)
        print("miss_rate", miss_rate)
        print("hit_rate", 1 - miss_rate)
        print("Finished processing your program trace, progress =", ((t+1) / len(trace)) * 100, "%")


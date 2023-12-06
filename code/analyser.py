import os
import json

'''
For each LRU, LFU and Radom
1. Miss Ratio vs Associativity
2. Miss Ratio vs Block Size
3. Block Size vs Associativity Heatmap
'''

result_dir = "../results/"

ascvsmr = {}
bsvsmr = {}
bsvsasc = {}

for i in os.listdir(result_dir):

    # if not os.path.isfile(result_dir + i):
    if not i.endswith(".txt"):
        continue

    print(i)

    cache_type, cache_size, associativity, block_size = i.split('.')[0].split('_')

    if cache_type not in ascvsmr:
        ascvsmr[cache_type] = {}
    if cache_type not in bsvsmr:
        bsvsmr[cache_type] = {}
    if cache_type not in bsvsasc:
        bsvsasc[cache_type] = {}

    fl = open(result_dir + i, 'r').read().split('\n')
    
    for j in fl:
        
        if not j.startswith('miss_rate'):
            continue
            
        # elif j.startswith('total cache misses'):
        #     pass
        
        # elif j.startswith('hit_rate'):
        #     pass

        miss_rate = float(j.replace('miss_rate', '').strip())

        if associativity not in ascvsmr[cache_type]:
            ascvsmr[cache_type][associativity] = { "average": 0, "count": 0 }

        ascvsmr[cache_type][associativity]["average"] = ((ascvsmr[cache_type][associativity]["average"] * ascvsmr[cache_type][associativity]["count"]) + miss_rate) / (ascvsmr[cache_type][associativity]["count"] + 1)
        ascvsmr[cache_type][associativity]["count"] += 1

        if block_size not in bsvsmr[cache_type]:
            bsvsmr[cache_type][block_size] = { "average": 0, "count": 0 }

        bsvsmr[cache_type][block_size]["average"] = ((bsvsmr[cache_type][block_size]["average"] * bsvsmr[cache_type][block_size]["count"]) + miss_rate) / (bsvsmr[cache_type][block_size]["count"] + 1)
        bsvsmr[cache_type][block_size]["count"] += 1

        if associativity not in bsvsasc[cache_type]:
            bsvsasc[cache_type][associativity] = {}

        if block_size not in bsvsasc[cache_type][associativity]:
            bsvsasc[cache_type][associativity][block_size] = { "average": 0, "count": 0 }
        
        bsvsasc[cache_type][associativity][block_size]["average"] = ((bsvsasc[cache_type][associativity][block_size]["average"] * bsvsasc[cache_type][associativity][block_size]["count"]) + miss_rate) / (bsvsasc[cache_type][associativity][block_size]["count"] + 1)
        bsvsasc[cache_type][associativity][block_size]["count"] += 1


print("Associativity vs Miss Rate\n\n", ascvsmr, "\n\n")
print("Block Size vs Miss Rate\n\n", bsvsmr, "\n\n")
print("Block Size vs Associativity\n\n", bsvsasc, "\n\n")


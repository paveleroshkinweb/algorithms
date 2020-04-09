from hash_map_chains import HashMapChains
import random
import hash
import math
from functools import reduce

size = 30007
random_range = 50000
keys_size = 37000
value = 5


def get_metrics(hash_fn):
    map = HashMapChains(size, hash_fn)
    for i in range(keys_size):
        random_key = random.randint(1, random_range)
        map.put(random_key, value)
    return {'average-chain-length': get_average_chain_length(map),
            'medium-chain-length': get_medium_chain_length(map),
            'max-chain-length': get_max_chain_length(map)}


def get_average_chain_length(map):
    buckets = map.buckets
    elements = 0
    count = 0
    for bucket in buckets:
        elements += len(bucket)
        if len(bucket) > 0:
            count += 1
    return elements / count


def get_medium_chain_length(map):
    buckets = list(filter(lambda bucket: len(bucket) > 0, map.buckets))
    buckets.sort(key=lambda bucket: len(bucket))
    return len(buckets[len(buckets) // 2])


def get_max_chain_length(map):
    return reduce(lambda max_chain, bucket: max(max_chain, len(bucket)), map.buckets, 0)


if __name__ == '__main__':
    hashes = [
              {'description': 'k % size', 'function': hash.hash1},
              {'description': '[size * {key * (sqrt(5) - 1) / 2}]', 'function': hash.hash3},
              {'description': '[size * {key * (sqrt(3) - 1) / 2}]', 'function': hash.hash2((math.sqrt(3) - 1) / 2)},
              {'description': '[size * {key * sqrt(3)}]', 'function': hash.hash2(math.sqrt(3))},
              {'description': '[size * {key * (sqrt(2) % 3)}]', 'function': hash.hash2(math.sqrt(2) % 3)},
              {'description': '[size * {key * (sqrt(5) % 3)}]', 'function': hash.hash2(math.sqrt(5) % 3)},
              {'description': '[size * {key * (sqrt(15))}]', 'function': hash.hash2(math.sqrt(15))}
             ]
    for hash_object in hashes:
        print(hash_object['description'])
        print(get_metrics(hash_object['function']))
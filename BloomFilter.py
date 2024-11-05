import mmh3  # for MurmurHash, install it via `pip install mmh3`
from bitarray import bitarray  # for bit manipulation, install it via `pip install bitarray`

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                return False
        return True

# Example Usage
size = 5000  # Size of bit array
hash_count = 7  # Number of hash functions
bloom = BloomFilter(size, hash_count)

# Adding items
bloom.add("apple")
bloom.add("banana")

# Checking if items are in the filter
print(bloom.contains("apple"))  # True, probably
print(bloom.contains("banana")) # True, probably
print(bloom.contains("grape"))  # False, definitely not in set

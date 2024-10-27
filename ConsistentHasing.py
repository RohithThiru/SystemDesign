import hashlib
from bisect import bisect, bisect_left

class ConsistentHashing:
    def __init__(self, num_replicas=3):
        """
        Initialize the consistent hashing ring with the specified number of replicas.
        
        :param num_replicas: Number of virtual nodes (replicas) for each real node.
        """
        self.num_replicas = num_replicas
        self.ring = {}
        self.sorted_keys = []

    def _hash(self, key):
        """
        Hash a key using SHA-256 and return an integer.
        
        :param key: Key to be hashed.
        :return: Integer hash value.
        """
        return int(hashlib.sha256(key.encode()).hexdigest(), 16)

    def add_node(self, node):
        """
        Add a real node to the hash ring along with its virtual nodes.
        
        :param node: Node to add to the hash ring.
        """
        for i in range(self.num_replicas):
            virtual_node_id = f"{node}-{i}"
            hash_val = self._hash(virtual_node_id)
            self.ring[hash_val] = node
            self.sorted_keys.append(hash_val)
        self.sorted_keys.sort()

    def remove_node(self, node):
        """
        Remove a real node and its virtual nodes from the hash ring.
        
        :param node: Node to remove from the hash ring.
        """
        for i in range(self.num_replicas):
            virtual_node_id = f"{node}-{i}"
            hash_val = self._hash(virtual_node_id)
            if hash_val in self.ring:
                del self.ring[hash_val]
                self.sorted_keys.remove(hash_val)

    def get_node(self, key):
        """
        Given a key, find the closest node in the hash ring in a clockwise manner.
        
        :param key: Key to map to a node.
        :return: Node responsible for the given key.
        """
        if not self.ring:
            return None
        hash_val = self._hash(key)
        idx = bisect(self.sorted_keys, hash_val) % len(self.sorted_keys)
        closest_hash = self.sorted_keys[idx]
        return self.ring[closest_hash]

# Example Usage
if __name__ == "__main__":
    ch = ConsistentHashing(num_replicas=3)
    
    # Adding nodes
    ch.add_node("Node1")
    ch.add_node("Node2")
    ch.add_node("Node3")

    # Get the node responsible for a given key
    print("Node responsible for key 'apple':", ch.get_node("apple"))
    print("Node responsible for key 'banana':", ch.get_node("banana"))
    print("Node responsible for key 'cherry':", ch.get_node("cherry"))

    # Removing a node
    ch.remove_node("Node2")
    print("Node responsible for key 'apple' after Node2 removal:", ch.get_node("apple"))

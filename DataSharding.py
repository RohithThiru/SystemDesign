# Define geographic shards
geographic_shards = {
    "North America": [],
    "Europe": [],
    "Asia": []
}

# Function to determine the shard based on geographic location
def get_geo_shard(region):
    return geographic_shards.get(region, None)

# Function to store user data based on geographic location
def store_geo_data(user_id, user_data, region):
    shard = get_geo_shard(region)
    if shard is not None:
        shard.append({'user_id': user_id, 'data': user_data})
        print(f"Stored data for User {user_id} in the {region} shard")
    else:
        print(f"Region {region} is not recognized")

# Example Usage
store_geo_data(101, {"name": "Alice", "age": 25}, "North America")
store_geo_data(202, {"name": "Bob", "age": 30}, "Europe")
store_geo_data(303, {"name": "Charlie", "age": 22}, "Asia")

print("\nGeographic Shards:")
for region, data in geographic_shards.items():
    print(f"{region} Shard: {data}")



# Define range shards
range_shards = {
    "0-1000": [],
    "1001-2000": [],
    "2001-3000": []
}

# Function to determine the shard based on user ID range
def get_range_shard(user_id):
    if 0 <= user_id <= 1000:
        return range_shards["0-1000"]
    elif 1001 <= user_id <= 2000:
        return range_shards["1001-2000"]
    elif 2001 <= user_id <= 3000:
        return range_shards["2001-3000"]
    return None

# Function to store user data based on user ID range
def store_range_data(user_id, user_data):
    shard = get_range_shard(user_id)
    if shard is not None:
        shard.append({'user_id': user_id, 'data': user_data})
        print(f"Stored data for User {user_id} in the {shard} shard")
    else:
        print(f"User ID {user_id} is out of range")

# Example Usage
store_range_data(101, {"name": "Alice", "age": 25})
store_range_data(1501, {"name": "Bob", "age": 30})
store_range_data(2501, {"name": "Charlie", "age": 22})

print("\nRange-based Shards:")
for range_key, data in range_shards.items():
    print(f"Shard {range_key}: {data}")




# Define hash-based shards
NUM_HASH_SHARDS = 4  # Total number of shards
hash_shards = {i: [] for i in range(NUM_HASH_SHARDS)}

# Function to determine the shard based on a hash of the user ID
def get_hash_shard(user_id):
    return user_id % NUM_HASH_SHARDS

# Function to store user data based on hash value
def store_hash_data(user_id, user_data):
    shard_id = get_hash_shard(user_id)
    hash_shards[shard_id].append({'user_id': user_id, 'data': user_data})
    print(f"Stored data for User {user_id} in Shard {shard_id}")

# Example Usage
store_hash_data(101, {"name": "Alice", "age": 25})
store_hash_data(202, {"name": "Bob", "age": 30})
store_hash_data(303, {"name": "Charlie", "age": 22})
store_hash_data(404, {"name": "Diana", "age": 28})

print("\nHash-based Shards:")
for shard_id, data in hash_shards.items():
    print(f"Shard {shard_id}: {data}")

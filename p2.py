import hashlib
import json
import time


def calculate_hash(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()


def create_block(index, user_data, metadata, previous_hash="0"):
    block = {
        "index": index,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "user_data": user_data,
        "metadata": metadata,
        "previous_hash": previous_hash
    }
    block["hash"] = calculate_hash(block)
    return block


blockchain = []


block1 = create_block(
    index=0,
    user_data={"user_id": "user1", "password": "abc123"},
    metadata={"cloud_paths": ["drive/docs/file1", "drive/photos/pic1"]},
    previous_hash="0"
)


block2 = create_block(
    index=1,
    user_data={"user_id": "user2", "password": "xyz789"},
    metadata={"cloud_paths": ["drive/videos/vid1", "drive/music/song1"]},
    previous_hash=block1["hash"]
)


blockchain.append(block1)
blockchain.append(block2)


print("\n Blockchain:")
for block in blockchain:
    print(json.dumps(block, indent=4))


print("\nChecking blockchain integrity...")
if block2["previous_hash"] == block1["hash"]:
    print("Blockchain is valid.")
else:
    print(" Blockchain has been tampered with!")


print("\n Modifying user1's password to 'hacked123'...")
block1["user_data"]["password"] = "hacked123"


print("\nRechecking integrity after tampering...")
if block2["previous_hash"] == calculate_hash(block1):
    print("Blockchain still valid.")
else:
    print(" Blockchain is broken due to tampering!")

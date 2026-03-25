from core.hashing import hash_file
from storage.db import load_chain

def verify_file(filepath):
    blockchain = load_chain()
    file_hash = hash_file(filepath)

    for block in blockchain.chain:
        if block.file_hash == file_hash:
            return True

    return False
from core.hashing import hash_file
from storage.db import load_chain, save_chain

def add_file(filepath):
    blockchain = load_chain()
    file_hash = hash_file(filepath)

    blockchain.add_block(file_hash, filepath)
    save_chain(blockchain)

    return file_hash
import json
from core.blockchain import Blockchain
from core.block import Block

DB_FILE = "storage/blockchain.json"

def save_chain(blockchain: Blockchain):
    with open(DB_FILE, "w") as f:
        json.dump([b.__dict__ for b in blockchain.chain], f, indent=4)

def load_chain():
    bc = Blockchain()
    bc.chain = []

    try:
        with open(DB_FILE, "r") as f:
            data = json.load(f)
            for b in data:
                block = Block(
                    b["index"],
                    b["file_hash"],
                    b["filename"],
                    b["previous_hash"]
                )
                block.timestamp = b["timestamp"]
                block.hash = b["hash"]
                bc.chain.append(block)
    except FileNotFoundError:
        bc.create_genesis_block()

    return bc
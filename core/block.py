import time
import json
from core.hashing import sha256

class Block:
    def __init__(self, index, file_hash, filename, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.file_hash = file_hash
        self.filename = filename
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block_string)
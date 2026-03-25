from core.block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, "0", "genesis", "0")
        self.chain.append(genesis)

    def add_block(self, file_hash, filename):
        last_block = self.chain[-1]
        new_block = Block(
            index=len(self.chain),
            file_hash=file_hash,
            filename=filename,
            previous_hash=last_block.hash
        )
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.compute_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True
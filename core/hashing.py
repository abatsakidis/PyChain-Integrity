import hashlib

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def hash_file(filepath: str) -> str:
    with open(filepath, "rb") as f:
        return sha256(f.read())
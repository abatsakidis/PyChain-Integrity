# 🔗 PyChain Integrity

A modular Python-based blockchain system for **file integrity verification**.  
This project uses blockchain principles to ensure that files have not been tampered with.

---

## 🚀 Features

- 📦 Add files to blockchain (store hash)
- 🔍 Verify file integrity
- 🧱 Immutable blockchain structure
- 💾 JSON-based persistent storage
- 🖥️ CLI interface
- 🧩 Modular architecture (production-style)

---

## 🧠 How It Works

1. A file is hashed using SHA-256
2. The hash is stored inside a new block
3. Each block is linked to the previous one
4. During verification:
   - The file is hashed again
   - The hash is compared with stored hashes

---

## 📁 Project Structure
```bash
pychain_integrity/
│
├── core/
│ ├── block.py
│ ├── blockchain.py
│ ├── hashing.py
│
├── services/
│ ├── file_service.py
│ ├── verification_service.py
│
├── storage/
│ ├── db.py
│ ├── blockchain.json
│
├── cli/
│ └── cli.py
│
├── utils/
│ ├── logger.py
│ └── config.py
│
├── main.py
└── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/pychain_integrity.git
cd pychain_integrity
```
No external dependencies required (uses Python standard library)

## ▶️ Usage

### Add a file to blockchain

```bash
python main.py add <file>
```

Example:
```bash
python main.py add document.pdf
```

Verify a file
```bash
python main.py verify <file>
```

Example:
```bash
python main.py verify document.pdf
```

## 📌 Output Examples

### Add file

Add file

 [+] File added with hash: 3a7bd3e2360a...

Verify file

[✔] File is VALID

or

[✘] File is TAMPERED or NOT FOUND


## 🔐 Security Concepts Used
-SHA-256 hashing
-Immutable data structures
-Blockchain linking (previous_hash)
-Integrity verification

Inspired by blockchain systems like Bitcoin and smart contract platforms like Ethereum.

## ⚠️ Limitations
-Single-node blockchain (not decentralized)
-No consensus mechanism
-No cryptographic signatures (yet)

## 🔥 Future Improvements
- Digital signatures (public/private keys)
- REST API (Flask / FastAPI)
- File monitoring (watchdog)
- GUI interface
- Distributed nodes (P2P)
- Logging system for cybersecurity use

## 🧪 Use Cases
-Document verification
-Digital notarization
-Log integrity (security / honeypots)
-Proof of existence

## 🛠️ Tech Stack
-Python 3.x
-hashlib
-json
-argparse

## 📄 License

MIT License

## 💡 Tip

This project is ideal for learning:

Blockchain fundamentals
Python architecture design
Security-focused development
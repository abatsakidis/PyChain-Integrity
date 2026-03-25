import argparse
from services.file_service import add_file
from services.verification_service import verify_file

def run():
    parser = argparse.ArgumentParser(description="Blockchain File Integrity Tool")
    subparsers = parser.add_subparsers(dest="command")

    add_cmd = subparsers.add_parser("add")
    add_cmd.add_argument("file")

    verify_cmd = subparsers.add_parser("verify")
    verify_cmd.add_argument("file")

    args = parser.parse_args()

    if args.command == "add":
        h = add_file(args.file)
        print(f"[+] File added with hash: {h}")

    elif args.command == "verify":
        if verify_file(args.file):
            print("[✔] File is VALID")
        else:
            print("[✘] File is TAMPERED or NOT FOUND")
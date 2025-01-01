#!/usr/bin/env python3

import argparse
import os

def count_bytes(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print(f"ccwc: {file_path}: No such file or directory")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Count bytes in a file.")
    parser.add_argument("-c", action="store_true", help="Count bytes in the file")
    parser.add_argument("file", help="The file to count bytes in")
    args = parser.parse_args()

    if args.c:
        byte_count = count_bytes(args.file)
        print(f"{byte_count:8} {args.file}")

if __name__ == "__main__":
    main()

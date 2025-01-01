#!/usr/bin/env python3
import sys
import argparse
import os

def count_bytes_from_content(content):
    return len(content.encode('utf-8'))

def count_lines_from_content(content):
    return content.count('\n')

def count_words_from_content(content):
    return len(content.split())

def count_bytes(file_path):
    try:
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        print(f"ccwc: {file_path}: No such file or directory")
        exit(1)

def count_lines(file_path):
    try:
        with open(file_path, "r") as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"ccwc: {file_path}: No such file or directory")
        exit(1)

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0

def count_characters(file_path):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return 0

def main():
    parser = argparse.ArgumentParser(description="Count bytes in a file.")
    parser.add_argument("-c", action="store_true", help="Count bytes in the file")
    parser.add_argument("-l", action="store_true", help="Count the number of lines in a file")
    parser.add_argument("-w", action="store_true", help="Count the number of words in a file")
    parser.add_argument("-m", action="store_true", help="Count the number of characters in a file")
    parser.add_argument("file", nargs="?", help="The file to process (optional; reads from stdin if not provided)")
    args = parser.parse_args()

    if not (args.c or args.l or args.w or args.m):
        args.c = True
        args.l = True
        args.w = True

    results = []
    if args.file:
        if args.c:
            byte_count = count_bytes(args.file)
            results.append(f"{byte_count:8}")

        if args.l:
            line_count = count_lines(args.file)
            results.append(f"{line_count:8}")

        if args.w:
            word_count = count_words(args.file)
            results.append(f"{word_count:8}")

        if args.m:
            character_count = count_characters(args.file)
            results.append(f"{character_count:8}")

        print("".join(results), args.file)

    else:
        content = sys.stdin.read()
        results = []
        if args.l:
            results.append(f"{count_lines_from_content(content):8}")
        if args.w:
            results.append(f"{count_words_from_content(content):8}")
        if args.c:
            results.append(f"{count_bytes_from_content(content):8}")
        print(" ".join(results))

if __name__ == "__main__":
    main()

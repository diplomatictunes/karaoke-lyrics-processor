#!/usr/bin/env python3

import codecs

def convert_to_utf8(file_path):
    # Read the file with the original encoding
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    # Write the content back to the same file in UTF-8 encoding
    with codecs.open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# Example usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python convert_to_utf8.py <file_path>")
        sys.exit(1)
    file_path = sys.argv[1]
    convert_to_utf8(file_path)

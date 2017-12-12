import sys
import string
from collections import Counter


def main():
    s = sys.stdin.read()
    c = Counter(s.lower())

    for char in string.ascii_lowercase:
        print(char, ":", c.get(char, 0))

if __name__ == "__main__":
    main()

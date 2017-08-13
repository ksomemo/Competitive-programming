import string

def solve(fav_chars, index):
    favs = [c for c in list(fav_chars) if c in string.ascii_lowercase]
    candidate = []
    for f1 in favs:
        for f2 in favs:
            candidate.append(f1 + f2)
    return candidate[index-1]

# template
import sys
def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

if __name__ == "__main__":
    fav_chars = input_str()
    index = input_int()
    result = solve(fav_chars, index)
    print(result)

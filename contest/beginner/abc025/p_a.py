import string

def solve(fav_chars, index):
    favs = [c for c in list(fav_chars) if c in string.ascii_lowercase]
    candidate = []
    for f1 in favs:
        for f2 in favs:
            candidate.append(f1 + f2)
    return candidate[index-1]

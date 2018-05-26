def main():
    es = input().split()
    b = input()
    ls = input().split()

    match = 0
    for e in es:
        if e in ls:
            match += 1

    isin_b = b in ls
    if match == 5:
        if isin_b:
            ans = 2
        else:
            ans = 3
    else:
        ans = {6: 1, 4: 4, 3: 5}.get(match, 0)

    print(ans)

    import sys
    print(match, file=sys.stderr)
    print(isin_b, file=sys.stderr)


if __name__ == '__main__':
    main()

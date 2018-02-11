def main():
    A = int(input())
    B = int(input())
    C = int(input())

    scores = (A, B, C)
    s = sorted(scores, reverse=True)
    for sc1 in scores:
        for rank, sc2 in enumerate(s, 1):
            if sc1 == sc2:
                print(rank)
                break

if __name__ == '__main__':
    main()

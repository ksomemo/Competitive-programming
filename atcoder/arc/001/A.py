def main():
    N = int(input())
    s = input()
    scores = [0] * 4

    for c in s:
        scores[int(c)-1] += 1

    print(max(scores), min(scores))


if __name__ == '__main__':
    main()

from collections import defaultdict


def main():
    N = int(input())

    A = map(int, input().split())
    B = map(int, input().split())
    scores = defaultdict(int)
    for a, b in zip(A, B):
        # k: -1
        if b == 0:
            b = -1
        scores[b] += a

    if scores[-1] >= max(scores.values()):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

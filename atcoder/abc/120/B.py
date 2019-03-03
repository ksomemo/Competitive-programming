def main():
    A, B, K = map(int, input().split())

    a_set = set([a for a in range(1, A+1) if A % a == 0])
    b_set = set([b for b in range(1, B+1) if B % b == 0])

    ab = list(a_set & b_set)
    ans = sorted(ab, reverse=True)[K-1]
    print(ans)


if __name__ == '__main__':
    main()

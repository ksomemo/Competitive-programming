def main():
    N = int(input())
    A1 = tuple(map(int, input().split()))
    A2 = tuple(map(int, input().split()))

    f(N, A1, A2)


def f(N, A1, A2):
    a1_cumsum = [A1[0]]
    for i in range(1, N):
        s = a1_cumsum[-1] + A1[i]
        a1_cumsum.append(s)

    a2_cumsum = [A2[0]]
    for i in range(1, N):
        s = a2_cumsum[-1] + A2[i]
        a2_cumsum.append(s)

    # iで下に移動した時
    ans = A1[0] + a2_cumsum[-1]
    for i in range(1, N):
        tmp_ans = a1_cumsum[i] + a2_cumsum[-1] - a2_cumsum[i - 1]
        ans = max(ans, tmp_ans)

    print(ans)

if __name__ == '__main__':
    main()

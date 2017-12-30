def main():
    N = int(input())
    C = []
    S = []
    F = []
    for i in range(1, N):
        c, s, f = map(int, input().split())
        C.append(c)
        S.append(s)
        F.append(f)

    # 逆順に計算して、結果の再利用
    res = [0] * N
    for i in range(1, N):
        res[i] = res[i - 1] + C[-i]
    # 後続の列車より早くない
    for i in range(1, N):
        res[i] = max(res[i - 1], res[i] + S[-i])

    for r in reversed(res):
        print(r)

if __name__ == '__main__':
    main()

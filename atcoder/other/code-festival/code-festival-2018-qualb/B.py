def main():
    N, X = map(int, input().split())
    a, b = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    # 顔の面白さは変動できないので高いものがよい
    # １番顔の面白い人はそれを増やすようにする
    ab = sorted(zip(a, b), key=lambda x: -x[1])
    ab[0] = (ab[0][0] + X, ab[0][1])

    ans = sum(_a * _b for _a, _b in ab)
    print(ans)


if __name__ == '__main__':
    main()

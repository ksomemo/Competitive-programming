def main():
    N = int(input())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))

    ans = 0
    # time: sum(t) seconds
    # t_n: v_n m/s 以内
    # a: +- 1 m/s^2
    # => ???
    # answer: max dist

    # 現時点の制限速度MAXで走ると距離は伸びるが
    # 次のスタート時点の制限速度を考慮しないとルール違反となる
    # 最初と最後は速度0
    # 次と比較しても次々にて速度Overする可能性がある…

    for i in range(N):
        pass
    print(ans)

if __name__ == '__main__':
    main()

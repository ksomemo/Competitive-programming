def main():
    """
    各民族(K_max=100)それぞれに対して
    目的地への移動可能日のうち最短を見つける(D_max=10^4)
    目的地はN_max=10^9

    各目的地への移動可能日(TLE)
    各日の移動可能目的地(10^4)
    上記に対する前日までに移動して待機おかないといけない場所

    A: start 2
    B: start 3
    1: 3-5: A:3-5, B:2
    2: 1-2: A:3-5, B:1-2
    3: 6-7: A:3-5, B:1-2
    4: 2-4: A:2-5, B:1-4

    """
    N, D, K = map(int, input().split())
    LR = [
        list(map(int, input().split()))
        for _ in range(D)
    ]
    ST = [
        list(map(int, input().split()))
        for _ in range(K)
    ]

    for s, t in ST:
        # 左右に動ける範囲を拡張していく(動かなくても良い)
        _l = s
        _r = s
        for d, (l, r) in enumerate(LR, 1):
            if l <= _l <= r:
                _l = l
            if l <= _r <= r:
                _r = r

            if _l <= t <= _r:
                print(d)
                break

if __name__ == '__main__':
    main()

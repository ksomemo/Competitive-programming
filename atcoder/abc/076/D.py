def main():
    N = int(input())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))

    ans = editorial(N, t, v)
    print(ans)
    # time: sum(t) seconds
    # t_n: v_n m/s 以内
    # a: +- 1 m/s^2
    # => ???
    # answer: max dist

    # 現時点の制限速度MAXで走ると距離は伸びるが
    # 次のスタート時点の制限速度を考慮しないとルール違反となる
    # 最初と最後は速度0
    # 次と比較しても次々にて速度Overする可能性がある…


def editorial(N, ts, vs):
    maxv = []
    for v, t in zip(vs, ts):
        maxv.extend([v] * 2 * t)

    # 入力例3
    # [0]-----------[12]-------------[26]-[28]
    # 0,6-----------6,2 -------------2,7 -7,0
    # 0,6-----------6,2 -------------2,7,7,7
    # 6,6---------6,2,2 -----------2,7,7,7,0
    # ↓
    # 6,6--------- 6,2,2 -----------2,7,7
    # 6 ---------- 2,2 -----------2,7,7,x
    # 前から0ベース
    # 後から0ベースでの比較
    maxv = [0] + [min(v1, v2) for v1, v2 in zip(maxv, maxv[1:])]
    maxv.append(0)

    max_t = len(maxv)
    bef_v = 0
    for i in range(max_t):
        bef_v = maxv[i] = min(maxv[i], bef_v + 0.5)
    aft_v = -0.5
    for i in range(max_t)[::-1]:
        aft_v = maxv[i] = min(maxv[i], aft_v + 0.5)

    ans = 0
    for v1, v2 in zip(maxv, maxv[1:]):
        ans += (v1 + v2) * 0.5 / 2

    return ans


def fix_maxv(maxv, max_t):
    """
    0123456789 -> t
      2--23--3 -> v

      のように見えるけど実際は違う

    """
    maxv = maxv[:]
    tmp = [None] * 3
    tmp[0] = maxv[:]
    bef_v = 0
    for i in range(max_t):
        bef_v = maxv[i] = min(maxv[i], bef_v + 0.5)

    # lastが 0.5にならず、0m/s になるように調整
    tmp[1] = maxv[:]
    aft_v = -0.5
    for i in range(max_t)[::-1]:
        aft_v = maxv[i] = min(maxv[i], aft_v + 0.5)
    tmp[2] = maxv[:]
    for i in range(max_t):
        print(*([0.5 + i/2] + [tmp[j][i] for j in range(3)]), sep="\t")

    return maxv


def editorial_WA(N, ts, vs):
    # サンプル4より、0.5刻みで考える必要あり
    maxv = []
    for v, t in zip(vs, ts):
        maxv.extend([v] * 2 * t)
    default_maxv = [v + 0.05 for v in maxv]

    max_t = sum(ts) * 2
    maxv = fix_maxv(maxv, max_t)

    import os
    # atcoder uname
    # posix.uname_result(sysname='Linux', nodename='imojudge-all', release='3.13.0-108-generic',
    #                    version='#155-Ubuntu SMP Wed Jan 11 16:58:52 UTC 2017',
    #                    machine='x86_64')
    local = "Darwin" in str(os.uname())
    if local:
        import matplotlib
        # matplotlib.use("Qt4Agg")
        matplotlib.use("TkAgg")
        import matplotlib.pyplot as plt
        real_ts = [i / 2 for i in range(1, len(maxv) + 1)]
        plt.plot(real_ts, maxv, color="red")
        plt.plot(real_ts, default_maxv, color="blue")
        plt.show()
        # plt.show(block=False)
        # plt.pause(.01)

    ans = 0
    # lastを0m/s に調整するために + [0]
    # しかし合計0.5 秒余計, この調整をやめることでlastが0.5m/s のまま
    # for t, (v1, v2) in enumerate(zip([0] + maxv, maxv + [0]), 1):
    for t, (v1, v2) in enumerate(zip([0] + maxv, maxv), 1):
        # 台形面積
        trapezoid = (v1 + v2) * 0.5 / 2
        ans += trapezoid
        if local:
            print(t / 2, v1, v2, trapezoid, ans, sep="\t")

    return ans


if __name__ == '__main__':
    main()

def main():
    """
    1 <= N <= 10^5
    1 <= K <= 10^12
    1 <= Ai <= 10^12
    """
    N, K = map(int, input().split())
    *A, = map(int, input().split())

    ans = editorial(N, K, A)
    if False:
        ans2 = TLE(N, K, A)
        ans3 = TLE2(N, K, A)
        assert ans2 == ans3
    ans4 = digit_dp(N, K, A)
    assert ans == ans4
    print(ans)


def TLE(N, K, A):
    ans = 0
    for x in range(K+1):
        xor_sum = 0
        for a in A:
            xor_sum += a ^ x
        ans = max(ans, xor_sum)

    return ans


def TLE2(N, K, A):
    """
    xor は各bit個別に計算できるので
    Aについて各bitが立っている個数を先に求めておく
    A <= 10^12 より A <= 2^40
    N <= 10^5 が 40 なので計算量は減るが
    K <= 10^12 なのでTLE

    >>> x = 10**12
    >>> p = 0
    >>> while x >= 2:
    ...    x /= 2
    ...    p += 1

    >>> x, p
    1.8189894035458565, 39

    >>> import math
    >>> math.log2(10**12)
    39.86313713864835

    ↓、嘘解法っぽい?
    """
    import math
    m = max(max(A), K)
    n_bit = math.ceil(math.log2(m))
    bit_counts = [0] * n_bit
    for a in A:
        for i in range(n_bit):
            if a & (1 << i):
                bit_counts[i] += 1

    ans = 0
    for x in range(K+1):
        xor_sum = 0
        for i, b in enumerate(bit_counts):
            if x & (1 << i):
                s = (1 << i) * (N - b)
            else:
                s = (1 << i) * b
            xor_sum += s

        ans = max(ans, xor_sum)

    return ans


def editorial(N, K, A):
    """
    N =3
    K =4:   100
    A1=3:   011
    A2=1:   001
    A3=1:   001
    ------------
    bit sum:013
     e.g.   110
    ------------
            421
            ***
            323
    ------------
          12+6+3 = 21
    これはX=6なので間違い

    X<=4: 

    """
    def cmp(a, b):
        """https://codegolf.stackexchange.com/questions/49778/how-can-i-use-cmpa-b-with-python3

        1,0: True  - False = 1 - 0 = 1
        1,1: False - False = 0 - 0 = 0
        0,1: False - True  = 0 - 1 = -1
        """
        return (a > b) - (a < b)

    ans = 0
    # K を超えないXをbitを使って探す
    # -> Kを超えるところから考えるほうがわかりやすい
    # Kを超えるbitから始めたとき
    for d in range(40, -2, -1):
        # d = -1 は X = K の場合
        # 上位のbitから処理、1であるbitなら対象
        # 基準の決め打ち？
        if d != -1 and (K & (1 << d)) == 0:
            print("continue")
            continue

        if d != -1:
            print("{:041b}".format(1 << d))
        # 各aについて上位bitから処理
        # X を決める
        tmp = 0
        bits = []
        for e in range(40, -1, -1):
            mask = 1 << e

            # bit=1である数, 外に出して前処理できる
            num = 0
            for a in A:
                if a & mask:
                    num += 1

            #print("\t", (e, d), cmp(e, d), num)
            # mask * num: num=1の数なので,0にしている
            # X≤K であるとは、
            # 上位ビットから見たときに X と K のビットが初めて一致しなかった桁が d であったとしたとき
            # この前提が組み込まれている
            # だからd=-1 のときずっと一致なので、X=K

            # 1. d より上位の桁については、X は K と一致
            # 2. d 桁目については X は 0 で、K は 1 である
            # 3. d より下位の桁については X はなんでもいい
            if e > d:
                # 上位bit
                # print("\t{:041b}".format(K))
                # print("\t{:041b}".format(mask))
                if K & mask:
                    # この桁では1がたっているので一致させるために1
                    # つまりnumは1基準なのでAの個数から0の個数を算出
                    tmp += mask * (N - num)
                    bits.append(1)
                else:
                    tmp += mask * num
                    bits.append(0)
            elif e == d:
                # 同じbit
                # 1を基準としているのでXのこのbitを0にしないと超えてしまう
                # 一致しないので0
                # 0を基準としていた場合、X>Kになる可能性がある
                tmp += mask * num
                bits.append(0)
            else:
                # 下位bit: 0,1のどちらでもいいので最大になるようにする
                m = max(num, N - num)
                tmp += mask * m
                bits.append(int(m != num))

        ans = max(ans, tmp)
        print("X = ", *bits, sep="")
        print("tmp =", tmp)

    return ans


def digit_dp(N, K, A):
    """桁DP: TODO

    http://drken1215.hatenablog.com/entry/2019/02/03/224200
    http://drken1215.hatenablog.com/entry/2019/02/04/013700
    https://qiita.com/nomikura/items/25883985ea148c3cf999
    """
    # dp[i桁見る][未満フラグ] = 総数
    dp = [[0] * 2 for _ in range(100)]

    for i in range(100):
        dp[i][0] = dp[i][1] = -1

    dp[40][0] = 0
    for d in range(40-1, -1, -1):
        mask = 1 << d
        num = 0
        for a in A:
            if a & mask:
                num += 1

        # 未満: 1つ上の桁
        if dp[d+1][1] >= 0:
            dp[d][1] = max(dp[d][1], dp[d+1][1] + mask * max(num, N-num))

        # 一致: 1つ上の桁
        if dp[d+1][0] >= 0:
            if K & (1 << d):
                dp[d][1] = max(dp[d][1], dp[d+1][0] + mask * num)
                dp[d][0] = max(dp[d][0], dp[d+1][0] + mask * (N-num))
            else:
                dp[d][0] = max(dp[d][0], dp[d+1][0] + mask * num)

    ans = max(dp[0][0], dp[0][1])
    return ans


def split_and_list_WA(N, K, A):
    """
    半分全列挙
    https://atcoder.jp/contests/abc117/submissions/4159666
    c++

    https://atcoder.jp/contests/abc117/submissions/4171940
    nim to python
    """
    # c[i]: A の要素のうち下から i 番目のビットが 1 であるものの個数
    c = [0] * (40+1)
    for a in A:
        for i in range(40):
            if ((a >> i) & 1) == 1:
                c[i] += 1

    def f_high(n):
        """n を左に 20 桁シフトしたものと A の要素の上位 20 ビットの xor の和"""
        m = n << 20
        result = 0
        for i in range(20, 40+1):
            if ((m >> i) & 1) == 1:
                result += (2 ** i) * (N - c[i])
            else:
                result += (2 ** i) * c[i]
        return result

    def f_low(n):
        """n と A の要素の下位 20 ビットの xor の和"""
        result = 0
        for i in range(0, 20):
            if ((n >> i) & 1) == 1:
                result += (2 ** i) * (N - c[i])
            else:
                result += (2 ** i) * c[i]
        return result

    # K の上位 / 下位 20 ビット
    k_high = K >> 20
    k_low = K & (1 << (20 - 1))

    # K < 2 ^ 20 なら全探索
    if k_high == 0:
        h_max = f_high(0)
        l_max = 0
        for n in range(K+1):
            l_max = max(l_max, f_low(n))
            ans = h_max + l_max
    else:
        # そうでないなら、上位と下位に分けて X を全探索
        # 1: X の上位が K に一致するならば、下位は K の下位より大きくならないようにとる
        # 2: X の上位が K より小さいならば、下位は 0..0 から 1..1 (20 桁) まで好きにとる
        # 二通り試して大きいほうが答え
        h_max1, h_max2, l_max1, l_max2 = (0, 0, 0, 0)
        for n in range(1 << (20 - 1) + 1):
            H = f_high(n)
            L = f_low(n)
            l_max1 = max(l_max1, L)
        if n < k_high:
            h_max1 = max(h_max1, H)
        if n == k_high:
            h_max2 = H
        if n <= k_low:
            l_max2 = max(l_max2, L)
        ans = max(h_max1 + l_max1, h_max2 + l_max2)

    return ans


if __name__ == '__main__':
    main()

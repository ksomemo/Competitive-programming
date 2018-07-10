def main():
    """
    1 <=  N <= 2 * 10^5
    1 <= ai <= 10^9
    """
    N = int(input())
    *A, = map(int, input().split())

    #ans = WA3(N, A)
    ans = editorial(N, A)
    print(ans)


def editorial(N, A):
    ans = 0
    C = sorted(a - i for i, a in enumerate(A, 1))
    if N % 2 == 1:
        b = C[N // 2]
    else:
        # 中央値だけど、整数？(=> 切り上げ下げどちらでもよい)
        s = C[N // 2 - 1] + C[N // 2 - 1]
        b = s // 2
        b = (s + 1) // 2

    ans = sum(abs(c - b) for c in C)
    return ans


def WA3(N, A):
    """
    Ci = Ai - i
    f(b) = sum( abs(Ci - b) )
    arg min f(b)

    abs(a-b)の最小化
        c-b or -(c-b)
        bを選べたとしてもN=2*10^5 より すべてについて最小化を見るとTLE
    """
    C = [a - i for i, a in enumerate(A, 1)]
    c1 = [c for c in C if c > 0]
    c2 = [c for c in C if c < 0]
    c0 = N - len(c1) - len(c2)
    # print(C)
    # print(c1)
    # print(c2)
    # print(c0)

    if c0 > len(c1) and c0 > len(c2):
        b = 0
    elif sum(c1) >= -sum(c2):
        b = min(c for c in C if c > 0)
    else:
        b = min(c for c in C if c < 0)
    # print(b)

    ans = sum(abs(c - b) for c in C)
    return ans


def WA2(N, A):
    """
    一番多い数を0に近づける => NG
    -10 -10 -10 11 11 12 12
      0   0   0 21 21 22 22
      +10: + 86

    -21 -21 -21 0 0 1 1
      -11: + 65

    -30 / 46
    +/-: どちらが多いか？
        平均が偏っているとダメでは？
           0:   -1   -2   3 100 => 106
          -3:   -4   -5   0  97 => 106
        -100: -101 -102 -97   0 => 300
    """
    ans = 0
    C = [a - i for i, a in enumerate(A, 1)]

    from collections import Counter
    co = Counter(C)
    b = co.most_common()[0][0]
    print(b)
    print(C)

    ans = sum(abs(c - b) for c in C)
    return ans


def WA(N, A):
    """
    直感: Aの平均値 => はずれ
    A-iの平均値
    """
    C = [a - i for i, a in enumerate(A, 1)]
    b = sum(C) // N
    print(b)
    print(C)
    ans = sum(abs(c - b) for c in C)

    return ans


if __name__ == '__main__':
    main()

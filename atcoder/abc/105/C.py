def main():
    """
    S: N の -2進数表現の条件

    1: S 0/1 からのみなる文字列
    2: S ='0' でなければSの先頭の文字は'1'
    3: S=S_k S_k-1...S_0
        S_0 * (-2)^0 + S_1 * (-2)^1 + ... + S_k * (-2)^k = N
    """
    N = int(input())
    ans = f(N)
    # ans = TLE(N)
    print(ans)


def TLE(N):
    if N == 0:
        return 0

    n_bit = 16 * 2
    for i in range(1, 2 ** n_bit):
        s = 0
        bits = []
        for j in range(n_bit):
            bit = (i & (1 << j))
            on = int(bit != 0)
            s += on * ((-2) ** j)
            bits.append(str(on))

        # print(i, s, "".join(bits[::-1]), sep="\t")

        if N == s:
            bits = bits[::-1]
            for k, b in enumerate(bits):
                if b == "1":
                    return "".join(bits[k:])

    return ""


def f(N):
    """
    bit全探索
    """
    if N == 0:
        return 0

    if N > 0:
        i = 0
    else:
        i = 1

    ans = 0
    while True:
        if N > 0 and (-2) ** i >= N:
            break
        elif N < 0 and (-2) ** i <= N:
            break
        i += 2

    print(2 ** i)

    return ans


if __name__ == '__main__':
    main()

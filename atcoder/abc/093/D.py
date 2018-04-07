def main():
    Q = int(input())
    AB = [
        map(int, input().split())
        for _ in range(Q)
    ]

    f(Q, AB)


def f(Q, AB):
    """
    参加者: 10^(10^10) => これは順位計算すらできない
    2回のコンテンスト、それぞれ異なる順位
    score = 1回目順位 * 2回目順位
    min = 1位*1位
    max = ビリ*ビリ

    1 <= A,B <= 10^9
    高橋max_score = 10^18

    例1-Q2:
        10,5->12

        A:10位より上の9人
            9位は5位以上でスコア低くなるが5位確定より4位以上
            8位以上は6以下でもOK
        B:5位より上の4人
            11-12:4位以上でOK
            13-16:3位以上
            17-24:2位以上
            25-49:1位
        4位以上: 4種類
        6位以下: 8種類
        よって12
    """
    for i in range(Q):
        A, B = AB[i]
        ans = solve(A, B)
        print(ans)


def solve(A, B):
    score = A * B
    a, b = sorted([A ,B], reverse=True)
    # sortは意味がない
    a, b = A, B

    # 1回目の順位がAより高い人
    if a == 1:
        x2 = 0
    else:
        min_rank2 = score // (a + 1)
        x2 = min_rank2 + 1
        for rank1 in range(min_rank2+1, a)[::-1]:
            # 高くても取らなきゃいけない2回目の最低順位
            rank2 = score // rank1
            if rank2 >= min_rank2:
                x2 -= 1
                break

    # 1回目の順位がAより低い人
    # 2回目の順位でチャンスのあるもの
    x1 = score // (a + 1)
    for rank2 in range(x1, 0, -1):
        # scoreを超える順位の組み合わせ
        break
        for rank1 in range(A+1, 10):
            sc = rank1 * rank2

    print("", x1, x2, sep="\t")
    ans = x1 + x2
    return ans


if __name__ == '__main__':
    main()

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


def editorial_pdf(A, B):
    """
    B=A+1
        score: A(A+1)
        A-1まで:ok
        A+1以上: socre=A(A+1) よりA-1以内
    
    C(C+1) または C^2 が積の最大値となることを利用する方法
    C^2<AB を満たす C を取ると、
        1: C^2<AB<C(C+1)
            A=3,B=13,√36=6<√39より、6^2<AB=39<6*7=42
        2: C^2   <C(C+1)<AB
            A=3,B=12,√36=6よりC=5,5^2=25<5*6=30<AB
    
        A  =B,C=A,A^2=A^2    C--する理由
        A+1=B,C=A,A^2<A(A+1) 
        のときはC=Aを含むため例外としている
    => これがベース
        だとしても、A-1までは確定
        A+1以降:
            要素数が奇数
            A+1,A+2,...,C-1,C,C+1,...,X
            X-A,.....................,1
        要素数が偶数
            A+1以降:A+1,A+2,...,C-1,C

        2C-1,2C-2が出て来る理由
            2(A-1)と同じ
                2(A-1):A=BのときA-1人Aより小さい人がいて、2回目についても同様に考えるため
            C(C+1)<=AB
                C位以内とC位以内
                ただしAとBが含まれるのでそれぞれ-1で2(C-1)
            C^2
                C位以内とC-1位以内

        1,    2,    ...,A-1
        A+B-1,A+B-2,...,B+1
            A+B-1?,not 2C-1?
            (C,C)が途中であらわれる
            (A+1,2C-A-1) 分かる:(1,2C-1)のあとA
            (A-1,B+1)    分からない
            (A-1)(B+1)
            = AB + (A-B) - 1 <=AB-1 (A<B)より
                まだ分からない 
            (A-1)B
            = AB -B
    """
    if A > B:
        A, B = B, A
        score = A * B
        if A == B or A + 1 == B:
            return (A - 1) * 2

    _C = score ** 0.5
    C = int(_C)
    if C == _C:
        C -= 1

    if C * (C + 1) >= score:
        return 2 * C - 2
    else:
        return 2 * C - 1


def editorial_movie(A, B):
    """
    https://www.youtube.com/watch?v=HDRfgn_UXLE
    http://banboooo.hatenablog.com/entry/2018/04/08/191942
    http://yamakasa3.hatenablog.com/entry/2018/04/22/000659
    http://kmjp.hatenablog.jp/entry/2018/04/07/0900
    http://ferin-tech.hatenablog.com/entry/2018/04/15/150222
    https://twitter.com/chiguri/status/982616224931577856

    score: AB
    1*x1 < AB => x1=AB-1 => x1=(AB-1)/1
    2*x2 < AB => x2=AB-1 => x2=(AB-1)/2
    ...
    (A-1)*x=AB           =>  x=(AB-1)/(A-1)
        ここまでA-1人
    A+1からAB-1まで
        A=Bのとき,2(A-1)
        平方完成での説明

    解説動画のクロスさせてABより小さくすることについて
    上から3人の例は、あくまで例
        A<=Bのとき A-B<=0 より
        (A-1)(B+1) = AB +  (A-B) - 1   <=AB-1
        (A-2)(B+2) = AB + 2(A-B) - 4   <=AB-4
        (A-x)(B+x) = AB + x(A-B) - x^2 <=AB-1 (x>=1)

        A+1
    """
    ans = 0

    return ans


def solve(A, B):
    score = A * B
    a, b = sorted([A, B], reverse=True)
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

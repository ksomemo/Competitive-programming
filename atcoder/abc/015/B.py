def main():
    N = int(input())
    A = map(int, input().split())

    s = 0
    b = 0
    for a in A:
        if a > 0:
            s += a
            b += 1

    ans = f1(s, b)

    print(ans)


def f1(a, b):
    """切り上げ math module使えばできるのは知ってる

    https://twitter.com/southerwolfie/status/950283947631558656
        (A + B - 1) / B: A+Bのoverflow
        (A - 1) / B + 1: A=0のときNG
    https://stackoverflow.com/questions/2745074/fast-ceiling-of-an-integer-division-in-c-c/2745763

    a / b の切り上げ
    (a + b): 商は1増える
    a = m * b + n (0 <= m, 0 <= n < b)
        1: a + b - 1 = (m + 1) * b +  n - 1
        2: (a+b-1)/b = (m + 1)     + (n - 1) / b

        n=0,aをbで割り切れるとき
        1: => (m+1)*b-1 より, m*b+(b-1), よって bの数はm+1でなくm
    """
    return (a + b - 1) // b


def f2(a, b):
    """四捨五入

    http://bttb.s1.valueserver.jp/wordpress/blog/2017/07/23/%E7%AB%B6%E3%83%97%E3%83%AD%E3%81%AE%E3%83%86%E3%82%AF%E3%83%8B%E3%83%83%E3%82%AF-%E5%89%B2%E3%82%8A%E7%AE%97%E3%81%AE%E5%88%87%E3%82%8A%E4%B8%8A%E3%81%92%E3%80%81%E5%9B%9B%E6%8D%A8%E4%BA%94%E5%85%A5/
    なんとなく分かるけど証明できない
    """
    return (a + (b // 2)) // b

if __name__ == '__main__':
    main()

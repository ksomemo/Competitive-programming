def main(N, aa):
    """
    a_i * a_(i+1) = 4k
        i=2n and i+1=2m
        i=4n or  i+1=4m

    half: 4m -> ok
    all: 2n -> ok

    example5
        2 7 1 8 2 8
          -     -
        2 2 1 8 7 8
    all2を作成
    残りhalfのパターン

    example2
        1 2 3 4
        2 1 3 4
          1 3 4

        all2, 最後の１つは２＊２にならないので以下でフォロー
        2, 4m, x, 4m
        2, 4m, x, 4m, x
    """
    n_m2 = 0
    n_m4 = 0
    n_m2_notm4 = 0
    for a in aa:
        is_m2 = a % 2 == 0
        is_m4 = a % 4 == 0

        n_m2 += int(is_m2)
        n_m4 += int(is_m4)
        n_m2_notm4 += int(is_m2 and not is_m4)

    if n_m2_notm4 == 0 and n_m4 >= N // 2:
        return "Yes"
    else:
        rest = N - n_m2_notm4 + 1
        if n_m4 >= rest // 2:
            return "Yes"
        else:
            return "No"


if __name__ == '__main__':
    N = int(input())
    aa = map(int, input().split())

    print(main(N, aa))

def main():
    NS = input()
    N = int(NS)

    s = sum(map(int, NS.split()))
    if N == 1:
        # 3番目の条件に一致するが合成数ではない
        print("Not Prime")
    elif is_prime(N):
        print("Prime")
    elif N % 2 == 1 and N % 10 != 5 and s % 3 != 0:
        print("Prime")
    else:
        print("Not Prime")


def is_prime(N):
    """試し割り
    """
    if N == 2:
        return True
    if N == 1 or N % 2 == 0:
        return False

    m = int(N ** 0.5)
    for i in range(3, m+1, 2):
        if N % i == 0:
            return False

    return True


def editorial(N):
    """
    昔のARCのAの位置づけふめいであるが
    ABCのAと同じならforなくてもいいのでO(1)で解けるように設定された？

    1. 各桁の和を求めなくていい
        – Nの1の位が偶数でない     -> 2の倍数判定
        – Nの1の位が5でない       -> 5の倍数判定
        - 各桁の和が3で割り切れない -> 3の倍数判定

            Nが2,3,5で割り切れないことと同値

    2. 素数判定不要
        – 2,3,5以外のNについて、Nが素数ならNは2,3,5で割り切れない
    """
    if N == 1:
        return False
    elif N in (2, 3, 5):
        return True
    elif N % 2 == 0 or N % 3 == 0 or N % 5 == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    main()

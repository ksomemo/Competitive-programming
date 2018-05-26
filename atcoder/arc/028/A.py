def main():
    N, A, B = map(int, input().split())

    for i in range(N):
        if i % 2 == 0:
            N -= A
            if N <= 0:
                print("Ant")
                break
        else:
            N -= B
            if N <= 0:
                print("Bug")
                break


def o1(N, A, B):
    """A+Bを1ターンと考える

    A+Bずつ減っていく
    最終ターンを考察 -> N % (A+B) < (A+B)
        あまり0ならBで終了している
        A以下ならAの番で終わり
        Aより大きいならBの番で終わり
    """
    if 0 < N % (A + B) <= A:
        print("Ant")
    else:
        print("Bug")


if __name__ == '__main__':
    main()

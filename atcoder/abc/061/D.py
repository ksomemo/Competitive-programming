def main():
    N, M = list(map(int, input().strip().split()))
    pos = 1
    socre = 0
    # node:a to node:b, weight: c
    l = [list(map(int, input().strip().split()))
         for _ in range(M)]
    # 閉路がある；
    # 重みが+の閉路：inf
    # 重みが-の閉路：ずっと通ってはいけない

    # 閉路がない；
    # 負の場合、最短で通る
    # 正の場合、最長で通る

if __name__ == '__main__':
    main()

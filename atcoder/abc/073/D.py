from itertools import permutations


def main():
    """
    とおり方
    2 <= N <= 200
    2 <= R <= min(8, N)
    より、
    最大でも 2 <= R <= 8
    8! = 40320

    道路
    1 <= M <= N * (N-1) / 2
    より、
    最大でも 100 * 199 = 19900

    調べ方
    rに現れない町を経由する可能性がある
    ある町Aからある町Bまでの最短距離を求める
    ABCの町を訪れるならば、
    A→B→C、
    B→C→A
    C→A→B
    の３パターン（組合せ）がある
    もちろん他の町を経由するかもしれない
        A→(D)→B→(E)→C
    """
    N, M, R = map(int, input().split())
    r = map(int, input().split())
    costs = {}
    for _ in range(M):
        a, b, c = map(int, input().split())
        costs[(a, b)] = c
    min_cost = float('inf')

    print(min_cost)

if __name__ == '__main__':
    main()

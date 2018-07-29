def main():
    a1, a2, a3 = map(int, input().split())

    ans = AC(a1, a2, a3)
    print(ans)


def editorial(a1, a2, a3):
    """
    愚直に解くと3点のうち、1点とその他の点の距離を求める。これの最小化
        もっと愚直にやるとa1,a2,a3の並べ方
        permutations([a1, a2, a3], 3)

    1,2,3 ならmax-min(中央との距離)
    3-1, 2-1 ではない(これはminとの距離、maxでも同様
    """
    ans = max([a1, a2, a3]) - min([a1, a2, a3])
    return ans


def AC(a1, a2, a3):
    c1 = abs(a3 - a1) + abs(a1 - a2)
    c2 = abs(a1 - a2) + abs(a2 - a3)
    c3 = abs(a2 - a3) + abs(a3 - a1)

    ans = min([c1, c2, c3])
    return ans


if __name__ == '__main__':
    main()

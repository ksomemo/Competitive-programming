from collections import Counter


def main():
    N = int(input())

    c = Counter(map(int, input().split()))
    mc = c.most_common()
    max_count = mc[0][1]
    m = filter(lambda t: t[1] == max_count, mc)
    # WA: すべて同じ個数だった時
    # 考慮できていない/Counterのkeyが辞書順とは限らない
    # level = list(m)[-1][0]
    level = max(dict(m).keys())
    print(level)

if __name__ == '__main__':
    main()

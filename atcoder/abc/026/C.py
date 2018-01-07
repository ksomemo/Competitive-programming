from collections import defaultdict


def main():
    """
    社長: i=1, salary=?
    部下なし: s=1
    部下あり: max(部下s) + min(部下s) + 1
    上司は1人
    上司の給料は,部下の給料をすべて確定しないと算出できない
    """
    N = int(input())
    B = [int(input()) for _ in range(N - 1)]

    # 社員の部下リスト
    subordinates = defaultdict(list)
    for i, b in enumerate(B, 2):
        subordinates[b].append(i)

    def salary(i):
        if not i in subordinates:
            return 1

        salaries = []
        for s in subordinates[i]:
            salaries.append(salary(s))

        return max(salaries) + min(salaries) + 1

    ans = salary(1)

    print(ans)


if __name__ == '__main__':
    main()

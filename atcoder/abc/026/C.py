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

    #dfs(N, B)
    #loop1_morau(N, B)
    loop2_kubaru(N, B)


def subs(B):
    # 社員の部下リスト
    subordinates = defaultdict(list)
    for i, b in enumerate(B, 2):
        subordinates[b].append(i)

    return subordinates


def dfs(N, B):
    subordinates = subs(B)

    def salary(i):
        if not i in subordinates:
            return 1

        salaries = []
        for s in subordinates[i]:
            salaries.append(salary(s))

        return max(salaries) + min(salaries) + 1

    ans = salary(1)

    print(ans)


def loop2_kubaru(N, B):
    p = [0] * (N + 1)
    max_p = [0] * (N + 1)
    min_p = [float("inf")] * (N + 1)

    # 部下のリストを用意せず、上司のmin/maxを更新
    for i in range(N, 0, -1):
        if max_p[i] == 0:
            p[i] = 1
        else:
            p[i] = max_p[i] + min_p[i] + 1

        if i == 1:
            boss = 0
        else:
            boss = B[i - 2]

        max_p[boss] = max(max_p[boss], p[i])
        min_p[boss] = min(min_p[boss], p[i])

    ans = p[1]
    print(ans)


def loop1_morau(N, B):
    p = [0] * (N + 1)
    subordinates = subs(B)

    # 上司は社員が自分より小さいので、逆順で処理すれば給料確定
    # 確定から埋める見慣れたDP
    for i in range(N, 0, -1):
        if not i in subordinates:
            p[i] = 1
            continue

        max_p, min_p = 0, float("inf")
        for k in subordinates[i]:
            max_p = max(max_p, p[k])
            min_p = min(min_p, p[k])

        p[i] = max_p + min_p + 1

    ans = p[1]
    print(ans)

if __name__ == '__main__':
    main()

def solve(N, M, edges):
    """
    TODO: implement
    """
    colors = ['r', 'b']

    start = ""
    return 'Yes'


class Edge():
    def __init__(self, idx, to, c):
        self.idx = idx
        self.to = to
        self.is_red = c == 'r'

    def __repr__(self):
        return "<%s: %s>" % (self.__class__, self.__dict__)


def check(idx, red):
    color = [0 for _ in range(N)]
    used = [False for _ in range(M)]

    if dfs(idx, red):
        return True
    for i in range(M):
        if not used[i]:
            return False
    return True


def dfs(idx, is_red):
    if color[idx] != 0:
        add = 1 if is_red else 2
        return color[idx] != add

    color[idx] |= 1 if is_red else 2
    for i in range(len(node[idx])):
        if used[node[idx][i].idx]:
            continue
        if node[idx][i].is_red == is_red:
            used[node[idx][i].idx] = True
            if dfs(node[idx][i].to, is_red ^ True):
                return True

    return False


if __name__ == '__main__':
    # 頂点, 辺
    N, M = map(int, input().split())
    color = [0 for _ in range(N)]
    used = [False for _ in range(M)]
    node = [[] for _ in range(N)]
    for i in range(M):
        a, b, color = input().split()
        a, b = int(a) - 1, int(b) - 1
        # 双方向行き来できるので、２つ
        node[a].append(Edge(i, b, color))
        node[b].append(Edge(i, a, color))

    from pprint import pprint
    pprint(node)

    for i in range(N):
        # 両方の色で試す
        if check(i, True) or check(i, False):
            print("Yes")
            exit(0)
    print("No")
#    result = solve(N, M, edges)
#    print(result)

def solve(N, M, edges):
    return 'Yes'

# util
def input_str():
    return input().strip('\n')

def input_int():
    return int(input_str())

def input_str_l(sep=None):
    return input_str().split(sep)

def input_int_l(sep=None):
    return list(map(int, input_str_l(sep)))

if __name__ == '__main__':
    N, M = input_int_l()
    edges = []
    for _ in range(N):
        vertex_a, vertex_b, color = input_str_l()
        edges.append([int(vertex_a), int(vertex_b), color])
    result = solve(N, M, edges)
    print(result)

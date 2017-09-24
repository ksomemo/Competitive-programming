import math


def main():
    X = int(input())
    Y = int(input())
    L = int(input())

    print(solve(X, Y, L))


def solve(X, Y, L):
    ans = 0
    if Y > 0:
        # north
        ans += math.ceil(abs(Y) / L)
    if X != 0 or Y < 0:
        # east, west, south
        ans += 1
    if X != 0:
        # east, west
        ans += math.ceil(abs(X) / L)
    if Y < 0:
        # south
        ans += 1
        ans += math.ceil(abs(Y) / L)

    return ans

if __name__ == '__main__':
    main()


def test():
    assert solve(0, 0, 2) == 0
    assert solve(0, 5, 2) == 3
    assert solve(0, -5, 2) == 5

    assert solve(5, 0, 2) == 4
    assert solve(-5, 0, 2) == 4

    assert solve(5, 5, 2) == 7
    assert solve(-5, 5, 2) == 7

    assert solve(5, -5, 2) == 8
    assert solve(-5, -5, 2) == 8

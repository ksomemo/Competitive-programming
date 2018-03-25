def main():
    N = int(input())
    *A, = map(int, input().split())

    f(N, A)


def f(N, A):
    """
    2 ≤ N ≤ 10^5
    −5000 ≤ Ai ≤ 5000 (1≤ i≤ N)

    第一印象: 累積和?
    →不要,合計のみ必要だった
    """
    costs = [abs(A[0])]
    for i in range(1, N):
        cost = abs(A[i] - A[i-1])
        costs.append(cost)

    # 0へ戻る
    cost_N_to_start = abs(A[-1])
    costs.append(cost_N_to_start)
    costs_cumsum = sum(costs)

    for i in range(N):
        total = costs_cumsum
        # skip: i-1 to i and i to i+1
        total -= (costs[i] + costs[i+1])

        # add: i-1 to i+1
        bef, aft = 0, 0
        if i - 1 >= 0:
            bef = A[i-1]
        if i + 1 < N:
            aft = A[i+1]
        total += abs(bef - aft)

        print(total)


if __name__ == '__main__':
    main()

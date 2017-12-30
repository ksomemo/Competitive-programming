def main():
    N, M = map(int, input().split())

    # Sから作れる数
    n_cc = M // 2
    n_scc = min(N, n_cc)

    # cから作れる数
    n_s = N - n_scc
    n_c = M - n_scc * 2
    n_add_scc = n_c // 4
    # n_c -= n_add_scc * 4

    ans = n_scc + n_add_scc

    print(ans)

if __name__ == '__main__':
    main()

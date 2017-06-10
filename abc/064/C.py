def main():
    N = int(input().strip())

    n_color = [0 for i in range(8)]
    n_free = 0
    rates = list(map(int, input().strip().split()))
    for r in rates:
        if r >= 3200:
            n_free += 1
        else:
            n_color[r // 400] += 1

    n_less_3200 = sum(1 for _ in n_color
                      if _ > 0)

    n_min = max(1, n_less_3200)
    n_max = n_less_3200 + n_free

    print(n_min, n_max)

if __name__ == '__main__':
    main()

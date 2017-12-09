def main():
    r, c = map(int, input().split())

    col_sums = [0] * c
    rows = [
        input()
        for n_r in range(r)
    ]

    for row in rows:
        row_sum = 0
        cols = map(int, row.split())
        for idx, col in enumerate(cols):
            col_sums[idx] += col
            row_sum += col

        print(row, end="")
        print("", row_sum)

    last_line = " ".join(map(str, col_sums))
    print(last_line, end="")
    print("", sum(col_sums))

if __name__ == "__main__":
    main()

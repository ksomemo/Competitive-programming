def main():
    n = int(input())
    n_b = 4
    n_f = 3
    n_r = 10

    from collections import defaultdict
    state = defaultdict(int)

    for _ in range(n):
        # b棟f階のr番目の部屋
        # v人が追加で入居したことを示します
        # vが負の値の場合、v人退去したことを示します。
        b, f, r, v = map(int, input().split())
        state[(b, f, r)] += v

    for b in range(1, n_b + 1):
        for f in range(1, n_f + 1):
            room_state = []
            for r in range(1, n_r + 1):
                room_state.append(state[(b, f, r)])
            print(" " + " ".join(map(str, room_state)))
        if b != n_b:
            print("#" * 20)


if __name__ == "__main__":
    main()

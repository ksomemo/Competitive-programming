def main():
    N, A, B = list(map(int, input().strip().split()))
    hs = [int(input().strip()) for _ in range(N)]

    answer = 0
    max_hp = max(hs)
    while max_hp > 0:
        idx_max = -1
        for i, hp in enumerate(hs):
            if hp <= 0:
                continue
            if idx_max == -1 and max_hp == hp:
                hs[i] -= A
                idx_max = i
            else:
                hs[i] -= B
        max_hp = max(hs)
        answer += 1

    print(answer)

if __name__ == '__main__':
    main()

def main():
    n = int(input())
    point_t = 0
    point_h = 0
    for _ in range(n):
        t, h = input().split()
        if t == h:
            point_t += 1
            point_h += 1
        elif t > h:
            point_t += 3
        else:
            point_h += 3

    print(point_t, point_h)

if __name__ == "__main__":
    main()

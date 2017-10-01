def main():
    px, py = map(int, input().split())
    qx, qy = map(int, input().split())

    dist_x = abs(px - qx)
    dist_y = abs(py - qy)
    print(dist_x / 2 + dist_y / 2)
if __name__ == '__main__':
    main()

def main():
    f_ver = map(int, input().split("."))
    j_ver = map(int, input().split("."))

    if tuple(f_ver) >= tuple(j_ver):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

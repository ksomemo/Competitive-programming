def main():
    abc = list(map(int, input().strip().split()))
    print(sum(sorted(abc)[:2]))

if __name__ == '__main__':
    main()

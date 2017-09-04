import sys


def main():
    args = sys.argv
    print(args, file=sys.stderr)
    sys.stderr.write("\n")

    N = int(input())
    print(0, N)

if __name__ == '__main__':
    main()

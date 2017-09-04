import math


def main():
    a, b = map(int, input().split())
    answer = int(math.ceil(b / a))
    print(answer)

if __name__ == '__main__':
    main()

def main():
    N = int(input())
    for i in range(1, N + 1):
        print(fizz_buzz(i))


def fizz_buzz(x):
    if x % (3 * 5) == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x


if __name__ == '__main__':
    main()

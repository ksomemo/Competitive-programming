def main():
    assert f(10) == 13
    assert f(f(10)) == 21
    assert f(f(f(10))) == 55

    print(f(f(f(20))))


def f(n):
    return (n ** 2 + 4) // 8


if __name__ == '__main__':
    main()

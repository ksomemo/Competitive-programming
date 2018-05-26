def main():
    S = input()
    
    ans = f(S) 
    print(ans)

def f(S):
    d = {
        'O': '0',
        'D': '0',
        'I': '1',
        'Z': '2',
        'S': '5',
        'B': '8',
    }

    ans = "".join(d.get(c, c) for c in S)
    return ans


def test_f():
    S = "IZSBOD"
    actual = "125800"
    assert f(S) == actual

    S = "1234567890"
    assert f(S) == S


if __name__ == '__main__':
    main()

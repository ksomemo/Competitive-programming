def main():
    S = input()

    ans = S.replace("Left", "<")
    ans = ans.replace("Right", ">")
    ans = ans.replace("AtCoder", "A")

    print(ans)

if __name__ == '__main__':
    main()

def main():
    s = input()
    t = input()

    s_ = sorted(s)
    t_ = sorted(t, reverse=True)
    if s_ < t_:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

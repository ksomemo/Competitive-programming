def main():
    S, t, u = input().split()

    t, u = int(t), int(u)
    gen = (c
           for i, c in enumerate(S)
           if i not in (t, u))

    print("".join(gen))

if __name__ == '__main__':
    main()

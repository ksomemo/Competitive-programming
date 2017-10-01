def main():
    S = input()
    for c1, c2 in zip("yukicoder", S):
        if c1 != c2:
            print(c1)

if __name__ == '__main__':
    main()

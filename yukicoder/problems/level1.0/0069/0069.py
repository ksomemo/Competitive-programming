def main():
    A = input()
    B = input()

    if sorted(A) == sorted(B):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

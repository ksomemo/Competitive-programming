def main():
    N_str = input().strip()
    if N_str == N_str[::-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

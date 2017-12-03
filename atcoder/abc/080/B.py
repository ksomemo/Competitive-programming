def main():
    N_str = input()

    N = int(N_str)
    sum_digit = sum(map(int, list(N_str)))

    if N % sum_digit == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

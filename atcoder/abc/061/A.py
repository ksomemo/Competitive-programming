def main():
    A, B, C = list(map(int, input().strip().split()))
    answer = "No"
    if A <= C <= B:
        answer = "Yes"
    print(answer)

if __name__ == '__main__':
    main()

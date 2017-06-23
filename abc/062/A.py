def main():
    x, y = list(map(int, input().strip().split()))
    groups = [
        [1, 3, 5, 7, 8, 10, 12],
        [4, 6, 9, 11],
        [2]
    ]
    answer = "No"
    for g in groups:
        if x in g and y in g:
            answer = "Yes"
            break
    print(answer)

if __name__ == '__main__':
    main()

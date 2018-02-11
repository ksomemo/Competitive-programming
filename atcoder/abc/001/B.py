def main():
    m = int(input())

    k = (m - m % 100) / 1000
    if m < 100:
        ans = 0
    elif 100 <= m <= 5000:
        ans = k * 10
    elif 6000 <= m <= 30000:
        ans = k + 50
    elif 35000 <= m <= 70000:
        ans = (k - 30) // 5 + 80
    elif m > 70000:
        ans = 89

    ans = str(int(ans)).zfill(2)
    print(ans)

if __name__ == '__main__':
    main()

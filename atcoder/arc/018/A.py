def main():
    H, BMI = map(float, input().split())

    W = BMI * H * H / (100 * 100)
    print(W)


if __name__ == '__main__':
    main()

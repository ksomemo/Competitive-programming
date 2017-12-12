import math


def main():
    r = float(input())
    print("{:.6f}".format(math.pi * r * r),
          "{:.6f}".format(2 * math.pi * r))

if __name__ == "__main__":
    main()

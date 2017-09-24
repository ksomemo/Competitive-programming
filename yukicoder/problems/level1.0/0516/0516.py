from collections import defaultdict


def main():
    S1 = input()
    S2 = input()
    S3 = input()

    d = defaultdict(int)
    d[S1] += 1
    d[S2] += 1
    d[S3] += 1

    if d["RED"] > d["BLUE"]:
        print("RED")
    else:
        print("BLUE")

if __name__ == '__main__':
    main()

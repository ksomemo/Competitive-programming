def main():
    while True:
        a, op, b = input().split()
        #a, b = int(a), int(b)
        if op == "?":
            break
        elif op == "/":
            op = "//"
        print(eval(a + op + b))

if __name__ == "__main__":
    main()
